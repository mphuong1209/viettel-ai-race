#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py - Improved Extract + QA pipeline (final)
- Enhanced, robust extract (headings, tables, images with placeholders & captions)
- Headings: convert any numbered headings (1., 1.1, 2.2.1) to Markdown (#, ##, ###, ####) and strip numbering
- Tables: keep as HTML blocks exactly (no extra blank-line splitting inside table)
- QA: hybrid retrieval (TF-IDF + BM25 + semantic) + cross-encoder rerank; choose SINGLE best option (highest score)
- Logging + per-question logs

Notes:
- Models used are small (<4B): sentence-transformers/all-MiniLM-L6-v2 and cross-encoder/ms-marco-MiniLM-L-6-v2
- DEVICE default is 'cpu'. If you have CUDA and want GPU, set DEVICE = 'cuda'.
"""
import os
import re
import glob
import time
import json
import logging
from pathlib import Path

import fitz  # PyMuPDF
import pdfplumber
from bs4 import BeautifulSoup
try:
    import camelot
    _HAS_CAMELOT = True
except Exception:
    _HAS_CAMELOT = False

import pandas as pd
from tqdm.auto import tqdm

from rank_bm25 import BM25Okapi
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, CrossEncoder, util
import numpy as np
import transformers
transformers.logging.set_verbosity_info()  # bật log download model HF

# -------------------------
# CONFIG
# -------------------------
# -------------------------
# CONFIG
# -------------------------
INPUT_DIR = "input"
OUTPUT_DIR = "submissions"
PDF_GLOB = "*.pdf"

# chunking
CHUNK_SENT_COUNT = 3
CHUNK_SENT_OVERLAP = 1   # new: sliding window overlap in sentences

TFIDF_MAX_FEATURES = 20000

# models (keep <4B). Recommended embedder for search:
EMBED_MODEL = "intfloat/multilingual-e5-small"   # => semantic search friendly, lightweight
RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"  # lightweight cross-encoder
DEVICE = "cpu"

# retrieval / rerank params
TOPN_RETRIEVE = 60   # number of chunks to retrieve for reranking (question-only)
RERANK_TOPK = 60     # how many per option to rerank (we rerank the same TOPN)
ABS_SCORE_THRESHOLD = 0.0

NEGATIVE_KEYWORDS = {"không", "không phải", "không đúng", "except", "trừ", "ngoại trừ", "not", "never", "none"}


os.makedirs(OUTPUT_DIR, exist_ok=True)
LOG_PATH = os.path.join(OUTPUT_DIR, "pipeline.log")
logging.basicConfig(level=logging.INFO, filename=LOG_PATH, filemode="w",
                    format="%(asctime)s [%(levelname)s] %(message)s")
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger().addHandler(console)

def log(msg, level=logging.INFO):
    logging.log(level, msg)

# -------------------------
# Utilities
# -------------------------

def safe_text(s):
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return s

# remove leading numeric outline like "1.", "1.1", "2.2.1", "(1)", "1)" or lines that are only numbers
_num_prefix_re = re.compile(r'^\s*(?:\d+(?:[\.\d]*)[\.)]?|(?:\(?\d+\)?)[\.)]?\s*-*\s*)+', flags=re.UNICODE)
_only_number_re = re.compile(r'^\s*\d+[\.)]?\s*$')

def clean_heading_text(text: str) -> str:
    """Strip common numbering prefixes from headings and trim."""
    if not text:
        return text
    t = text.strip()
    # if line is just a number or a number+dot, return empty to skip
    if _only_number_re.match(t):
        return ""
    # remove patterns like '1. ', '1.1 ', '2.2.1 ', '(1) ', '1) '
    t2 = _num_prefix_re.sub('', t)
    return t2.strip()

def split_sentences(text):
    if not text:
        return []
    s = re.sub(r'\r\n', '\n', text)
    s = re.sub(r'\n\s+\n', '\n\n', s)
    parts = re.split(r'(?<=[\.!?;:])\s+(?=[\w\(\[\u00C0-\u017F])|[\n]{2,}', s)
    parts = [p.strip() for p in parts if p and len(p.strip())>0]
    return parts

def make_dirs(path):
    os.makedirs(path, exist_ok=True)

# -------------------------
# Extract helpers
# -------------------------

def extract_images_with_pymupdf(doc, page_index, images_dir, img_counter):
    out = []
    page = doc[page_index]
    try:
        pdict = page.get_text("dict")
    except Exception:
        pdict = {}
    used_xrefs = set()
    for block in pdict.get("blocks", []):
        if block.get("type") == 1:
            xref = block.get("xref") or block.get("image")
            try:
                xref = int(xref)
            except Exception:
                xref = None
            bbox = block.get("bbox", None)
            y_center = None
            if bbox and len(bbox) >= 4:
                y_center = (bbox[1] + bbox[3]) / 2.0
            if xref:
                try:
                    base = doc.extract_image(xref)
                    image_bytes = base["image"]
                    ext = base.get("ext", "png")
                    fname = f"image_{img_counter}.{ext}"
                    out_path = os.path.join(images_dir, fname)
                    with open(out_path, "wb") as fh:
                        fh.write(image_bytes)
                    out.append((fname, y_center))
                    img_counter += 1
                    used_xrefs.add(xref)
                except Exception as e:
                    log(f"[WARN] image extract by xref failed p{page_index+1}: {e}", logging.WARNING)
    if not out:
        try:
            img_list = page.get_images(full=True)
        except Exception:
            img_list = []
        for imginfo in img_list:
            xref = imginfo[0]
            if xref in used_xrefs:
                continue
            try:
                base = doc.extract_image(xref)
                image_bytes = base["image"]
                ext = base.get("ext", "png")
                fname = f"image_{img_counter}.{ext}"
                out_path = os.path.join(images_dir, fname)
                with open(out_path, "wb") as fh:
                    fh.write(image_bytes)
                out.append((fname, None))
                img_counter += 1
            except Exception as e:
                log(f"[WARN] image extract fallback error: {e}", logging.WARNING)
    return img_counter, out

def detect_headings_from_page(page_dict):
    sizes = []
    lines = []
    for block in page_dict.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            line_text = []
            fonts = []
            for span in line.get("spans", []):
                txt = span.get("text", "")
                if txt.strip():
                    if line_text and not line_text[-1].endswith(" ") and not txt.startswith(" "):
                        line_text.append(" ")
                    line_text.append(txt)
                    fonts.append((span.get("size", 0), span.get("flags", 0), span.get("font", "")))
                    sizes.append(span.get("size", 0))
            if line_text:
                joined = "".join(line_text).strip()
                if joined:
                    lines.append((joined, fonts))
    avg_size = (sum(sizes) / len(sizes)) if sizes else 0.0
    result = []
    for text, fonts in lines:
        if not fonts:
            result.append((0, text))
            continue
        max_size = max((f[0] for f in fonts))
        bold_flag = any(((f[1] & 2) != 0) or ('Bold' in (f[2] or "")) for f in fonts)
        level = 0
        if avg_size > 0 and max_size >= avg_size * 1.6:
            level = 1
        elif avg_size > 0 and max_size >= avg_size * 1.25:
            level = 2
        elif bold_flag and max_size >= avg_size * 1.10:
            level = 3
        else:
            level = 0
        result.append((level, text))
    return result

def extract_tables_from_pdf(pdf_path, page_number):
    html_tables = []
    if _HAS_CAMELOT:
        try:
            tables = camelot.read_pdf(pdf_path, pages=str(page_number))
            for t in tables:
                html_tables.append(t.df.to_html(index=False, header=True))
            if html_tables:
                return html_tables
        except Exception as e:
            logging.debug(f"Camelot failed on {pdf_path} page {page_number}: {e}")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            if page_number - 1 < len(pdf.pages):
                page = pdf.pages[page_number - 1]
                pls = page.extract_tables()
                for table in pls:
                    soup = BeautifulSoup("", "html.parser")
                    table_tag = soup.new_tag("table")
                    if not table:
                        continue
                    thead = soup.new_tag("thead")
                    tr = soup.new_tag("tr")
                    for cell in table[0]:
                        th = soup.new_tag("th")
                        th.string = "" if cell is None else str(cell)
                        tr.append(th)
                    thead.append(tr)
                    table_tag.append(thead)
                    tbody = soup.new_tag("tbody")
                    for row in table[1:]:
                        tr = soup.new_tag("tr")
                        for cell in row:
                            td = soup.new_tag("td")
                            td.string = "" if cell is None else str(cell)
                            tr.append(td)
                        tbody.append(tr)
                    table_tag.append(tbody)
                    # IMPORTANT: append raw HTML without inserting extra blank lines inside
                    html_tables.append(str(table_tag))
    except Exception as e:
        logging.debug(f"pdfplumber table extraction error: {e}")
    return html_tables

def find_caption_nearby(text_blocks, image_y, tolerance=40):
    if image_y is None:
        return None
    candidates = []
    for by, btext in text_blocks:
        if by is None:
            continue
        if abs(by - image_y) <= tolerance:
            if re.search(r'\b(Hình|Hinh|Figure|Fig\.|Ảnh|Image)\b', btext, flags=re.IGNORECASE):
                candidates.append((abs(by - image_y), btext))
    if candidates:
        candidates.sort(key=lambda x: x[0])
        return candidates[0][1]
    return None

# -------------------------
# Main extract function
# -------------------------

def extract_pdf_to_md_enhanced(pdf_path, out_root):
    pdf_name = Path(pdf_path).stem
    out_folder = os.path.join(out_root, pdf_name)
    images_dir = os.path.join(out_folder, "images")
    make_dirs(images_dir)
    make_dirs(out_folder)

    doc = fitz.open(pdf_path)
    content_parts = [f"# {pdf_name}\n\n"]
    img_counter = 1

    for p_idx in range(len(doc)):
        page = doc[p_idx]
        try:
            pdict = page.get_text("dict")
        except Exception:
            pdict = {}

        text_blocks_centers = []
        for block in pdict.get("blocks", []):
            if block.get("type") != 0:
                continue
            ys = []
            block_text_lines = []
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    bbox = span.get("bbox", None)
                    if bbox and len(bbox) >= 4:
                        ys.append((bbox[1] + bbox[3]) / 2)
                    block_text_lines.append(span.get("text", ""))
                block_text_lines.append("\n")
            yc = (sum(ys)/len(ys)) if ys else None
            block_text = "".join(block_text_lines).strip()
            if block_text:
                text_blocks_centers.append((yc, block_text))

        page_headings = detect_headings_from_page(pdict)
        for level, line in page_headings:
            if not line or line.strip() == "":
                continue
            clean = clean_heading_text(line)
            if not clean:
                continue
            # detect simple formulas like E = mc^2 → wrap with $...$
            clean = re.sub(r'([A-Za-z0-9\s\+\-\*/=\(\)\[\]\{\}]+)=([A-Za-z0-9\s\+\-\*/=\(\)\[\]\{\}]+)', r'$\1=\2$', clean)
            if level == 1:
                content_parts.append(f"# {clean}\n\n")
            elif level == 2:
                content_parts.append(f"## {clean}\n\n")
            elif level == 3:
                content_parts.append(f"### {clean}\n\n")
            # bỏ thêm line thường ở else → tránh text lặp


        # Tables: insert HTML blocks exactly, with a single trailing newline (no extra blank lines inside)
        try:
            tables_html = extract_tables_from_pdf(pdf_path, p_idx+1)
            for t_html in tables_html:
                content_parts.append(t_html + "\n\n")  # tách bảng và text rõ ràng

        except Exception as e:
            logging.debug(f"No tables on page {p_idx+1} or extraction failed: {e}")

        # Images
        try:
            img_counter, extracted = extract_images_with_pymupdf(doc, p_idx, images_dir, img_counter)
            for fname, y_center in extracted:
                match = re.search(r'image_(\d+)', fname)
                num = int(match.group(1)) if match else img_counter
                placeholder = f"|<image_{num}>|"
                caption = find_caption_nearby(text_blocks_centers, y_center, tolerance=60)
                content_parts.append(placeholder + "\n\n")
                if caption:
                    content_parts.append(f"_**{caption}**_\n\n")
        except Exception as e:
            log(f"[WARN] image extraction on page {p_idx+1} failed: {e}", logging.WARNING)

        # page separator
        content_parts.append("\n")

    try:
        doc.close()
    except Exception:
        pass

    md_path = os.path.join(out_folder, "main.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("".join(content_parts))
    log(f"[EXTRACT] Wrote {md_path} (images in {images_dir})")
    return out_folder, md_path

# -------------------------
# Chunking & Index building
# -------------------------

def build_chunks_per_doc(md_paths, chunk_sent_count=CHUNK_SENT_COUNT, overlap=CHUNK_SENT_OVERLAP):
    chunks = []
    meta = []
    for md in md_paths:
        with open(md, "r", encoding="utf-8") as f:
            text = f.read()
        # remove title lines starting with '# <filename>'
        text_body = re.sub(r'^#\s.*\n+', '', text, flags=re.MULTILINE)
        # tách theo đoạn markdown hoặc bảng để giữ ngữ cảnh
        parts = re.split(r'(?=\n#|\n##|\n###|<table|</table>)', text_body)
        clean_parts = [p.strip() for p in parts if len(p.strip()) > 0]

        for p in clean_parts:
            if len(p) < 50:
                continue
            chunks.append(p)
            meta.append({"md_path": md, "start_sent": 0})

        # filter tiny sents
        sents = split_sentences(text_body)
        sents = [s for s in sents if len(s) > 20]
        if not sents:
            # fallback to first 1000 chars as a single chunk
            snippet = text_body.strip()[:1000]
            if snippet:
                chunks.append(snippet)
                meta.append({"md_path": md, "start_sent": 0})
            continue

        step = max(1, chunk_sent_count - overlap)
        for i in range(0, max(1, len(sents)), step):
            window = sents[i:i+chunk_sent_count]
            chunk = " ".join(window).strip()
            if len(chunk) >= 40:
                chunks.append(chunk)
                meta.append({"md_path": md, "start_sent": i})
            if i + chunk_sent_count >= len(sents):
                break
    if not chunks:
        # final fallback
        for md in md_paths:
            with open(md, "r", encoding="utf-8") as f:
                t = f.read()[:1000]
            chunks.append(t)
            meta.append({"md_path": md, "start_sent": 0})
    return chunks, meta


# -------------------------
# QA: retrievers + rerank (choose SINGLE best)
# -------------------------
def prepare_retrievers(chunks):
    log("[INDEX] Building TF-IDF matrix...")
    vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=TFIDF_MAX_FEATURES)
    tfidf_matrix = vectorizer.fit_transform(chunks)

    log("[INDEX] Building BM25 index...")
    tokenized = [re.findall(r"\w+", c.lower()) for c in chunks]
    if not chunks:
        raise ValueError("[INDEX] No valid chunks to build BM25 index!")
    bm25 = BM25Okapi(tokenized)

    log(f"[INDEX] Loading embedder {EMBED_MODEL} on {DEVICE} ...")
    embedder = SentenceTransformer(EMBED_MODEL, device=DEVICE)
    log(f"[INDEX] Encoding {len(chunks)} chunks with embedder (progress bar shown)...")
    chunk_embeds = embedder.encode(
        chunks,
        batch_size=64,
        convert_to_tensor=True,
        show_progress_bar=True,  # <-- bật progress bar
        normalize_embeddings=True
    )
    log(f"[INDEX] Embedder encoding done.")

    log(f"[INDEX] Loading reranker {RERANKER_MODEL} on {DEVICE} ...")
    reranker = CrossEncoder(RERANKER_MODEL, device=DEVICE)
    log(f"[INDEX] Reranker model loaded.")

    return {
        "vectorizer": vectorizer,
        "tfidf": tfidf_matrix,
        "bm25": bm25,
        "tokenized_chunks": tokenized,
        "embedder": embedder,
        "chunk_embeds": chunk_embeds,
        "reranker": reranker
    }

from math import exp

def softmax(x):
    # numerically stable softmax
    x = np.array(x, dtype=float)
    if x.size == 0:
        return x
    e_x = np.exp(x - np.max(x))
    return e_x / (e_x.sum() + 1e-12)

def normalize_vec(x):
    if x is None or len(x) == 0:
        return np.zeros_like(x)
    x = np.array(x, dtype=float)
    rng = x.max() - x.min()
    if rng <= 0:
        return np.zeros_like(x)
    return (x - x.min()) / (rng + 1e-12)

def hybrid_retrieve_and_answer(question_row, retrievers, chunks, chunk_meta, topk=8):
    qtext = safe_text(question_row.get("Question", ""))
    options = [safe_text(question_row.get(k, "")) for k in ["A","B","C","D"]]

    # 1) Retrieve using QUESTION ONLY (not question+option)
    # TF-IDF
    try:
        qvec = retrievers["vectorizer"].transform([qtext])
        sims_tfidf = cosine_similarity(qvec, retrievers["tfidf"]).reshape(-1)  # (n_chunks,)
    except Exception:
        sims_tfidf = np.zeros(len(chunks))

    # semantic
    try:
        q_emb = retrievers["embedder"].encode([qtext], convert_to_tensor=True, normalize_embeddings=True)
        sem_sims = util.cos_sim(q_emb, retrievers["chunk_embeds"]).cpu().numpy().reshape(-1)
    except Exception:
        sem_sims = np.zeros(len(chunks))

    # BM25
    try:
        tokens = re.findall(r"\w+", qtext.lower())
        bm25_scores = retrievers["bm25"].get_scores(tokens) if tokens else np.zeros(len(chunks))
    except Exception:
        bm25_scores = np.zeros(len(chunks))

    # normalize each signal
    tf_n = normalize_vec(sims_tfidf)
    sem_n = normalize_vec(sem_sims)
    bm_n = normalize_vec(bm25_scores)

    # combine into question-level chunk scores
    # weights tuned: semantic strongest, tfidf next, bm25 small
    combined_q_scores = 0.6 * sem_n + 0.3 * tf_n + 0.1 * bm_n
    # pick topN indices to rerank
    topN = min(len(chunks), TOPN_RETRIEVE)
    top_inds = np.argsort(combined_q_scores)[-topN:][::-1]

    # prepare per-option rerank: rerank same top_inds for fairness
    option_final_scores = []
    per_option_details = []

    # For memory, batch the pairs per option
    for opt_idx, opt in enumerate(options):
        # build pairs: (query_for_reranker, chunk)
        # Use query format that includes question and option explicitly (helps cross-encoder)
        pairs = []
        for j in top_inds:
            q_for_rerank = f"{qtext} [SEP] {opt}"
            pairs.append((q_for_rerank, chunks[j]))
        # run reranker in batch
        try:
            rerank_scores = retrievers["reranker"].predict(pairs, batch_size=32)
            rerank_scores = np.array(rerank_scores, dtype=float)
            # normalize rerank scores via min-max then softmax for stability
            if rerank_scores.size > 0:
                rerank_n = normalize_vec(rerank_scores)
                rerank_soft = softmax(rerank_scores)
            else:
                rerank_n = np.zeros_like(rerank_scores)
                rerank_soft = np.zeros_like(rerank_scores)
        except Exception as e:
            log(f"[WARN] reranker failed for option {opt_idx}: {e}", logging.WARNING)
            rerank_scores = np.zeros(len(pairs))
            rerank_n = np.zeros_like(rerank_scores)
            rerank_soft = np.zeros_like(rerank_scores)

        # Now combine rerank signals with combined_q_scores (only for those top_inds)
        combo_scores_for_top = combined_q_scores[top_inds]
        combo_norm = normalize_vec(combo_scores_for_top)

        # final scoring for this option:
        # - use both max and mean of rerank_n (stable vs. best)
        # - incorporate softmax mass as another signal (how concentrated)
        # weights: reranker dominant
        if rerank_n.size > 0:
            score_max = float(np.max(rerank_n))
            score_mean = float(np.mean(rerank_n))
            score_softmass = float(np.max(rerank_soft))  # how strongly one chunk stands out
        else:
            score_max = 0.0
            score_mean = 0.0
            score_softmass = 0.0

        # also include combo_norm max to favor chunks that retrieval thought relevant
        combo_max = float(np.max(combo_norm)) if combo_norm.size > 0 else 0.0

        final_score = 0.80 * score_max + 0.12 * score_mean + 0.03 * score_softmass + 0.05 * combo_max

        per_option_details.append({
            "top_chunk_indices": top_inds.tolist(),
            "rerank_scores": rerank_scores.tolist(),
            "retrieval_scores": combo_scores_for_top.tolist()
        })
        option_final_scores.append(final_score)

    # Negative question handling: if question contains negative keywords, choose lowest-scoring option
    qlower = qtext.lower()
    is_negative = any(k in qlower for k in NEGATIVE_KEYWORDS)

    scores = np.array(option_final_scores, dtype=float)
    if scores.size == 0:
        return ["A"], {}

    # Chuẩn hóa scores về [0,1]
    scores_n = (scores - scores.min()) / (scores.max() - scores.min() + 1e-8)

    # Tính độ chênh giữa max và các score khác
    best_val = scores_n.max()
    diffs = best_val - scores_n

    # Ngưỡng chọn thêm đáp án phụ (0.08–0.12 là hợp lý)
    # nghĩa là nếu score chênh < 0.1 so với max => có thể là đáp án đúng phụ
    threshold_gap = 0.10

    if is_negative:
        # nếu câu phủ định → chọn các đáp án thấp nhất
        chosen = [chr(65 + i) for i, s in enumerate(scores_n) if s <= (1 - best_val + threshold_gap)]
    else:
        chosen = [chr(65 + i) for i, d in enumerate(diffs) if d <= threshold_gap]

    # fallback: nếu không có hoặc chọn quá nhiều
    if not chosen:
        chosen = [chr(65 + int(np.argmax(scores_n)))]
    elif len(chosen) > 3:
        # tránh lấy quá 3 đáp án
        chosen = sorted(chosen, key=lambda c: -scores_n[ord(c)-65])[:3]
        # Log kết quả từng câu hỏi (hỗ trợ debug)
    try:
        score_str = ", ".join([f"{chr(65+i)}={s:.2f}" for i, s in enumerate(scores_n)])
        log(f"[QA-DEBUG] chosen={chosen} | scores_norm=[{score_str}]")
    except Exception:
        pass

    details = {
        "option_final_scores": option_final_scores,
        "per_option_details": per_option_details,
        "chosen": chosen,
        "top_inds": top_inds.tolist()
    }
    return chosen, details

# -------------------------
# Output writer
# -------------------------

def build_answer_md(output_dir, processed_folders, df_questions, answers):
    parts = ["### TASK EXTRACT\n"]
    for _pdf, folder, md_path in sorted(processed_folders, key=lambda x: os.path.basename(x[1])):
        pdf_name = os.path.basename(folder)
        parts.append(f"# {pdf_name}\n")
        with open(md_path, "r", encoding="utf-8") as f:
            parts.append(f.read().strip() + "\n\n")

    parts.append("### TASK QA\n")
    parts.append("num_correct,answers\n")

    for ans in answers:
        # trường hợp không có đáp án
        if not ans:
            parts.append("0,\n")
            continue

        # đảm bảo ans là list hoặc tuple
        if isinstance(ans, (list, tuple)):
            if len(ans) == 0:
                parts.append("0,\n")
            elif len(ans) == 1:
                # chỉ 1 đáp án → 1,A
                parts.append(f"1,{ans[0]}\n")
            else:
                # ⭐ chỗ này ghi kiểu 2,"A,B" hoặc 3,"A,B,C"
                joined = ",".join(ans)
                parts.append(f"{len(ans)},\"{joined}\"\n")

        else:
            # fallback nếu ans là string (phòng lỗi)
            s = str(ans).strip()
            if s == "":
                parts.append("0,\n")
            else:
                parts.append(f"1,{s}\n")

    answer_path = os.path.join(output_dir, "answer.md")
    with open(answer_path, "w", encoding="utf-8") as f:
        f.write("".join(parts))
    log(f"[OUTPUT] Wrote {answer_path}")
    return answer_path

# -------------------------
# Main orchestration
# -------------------------

def main():
    t0 = time.time()
    log("[START] Pipeline starting")

    pdf_paths = sorted(glob.glob(os.path.join(INPUT_DIR, PDF_GLOB)))
    if not pdf_paths:
        log(f"[ERROR] No PDFs found in {INPUT_DIR} matching {PDF_GLOB}", logging.ERROR)
        return

    processed = []
    log("[EXTRACT] Starting extraction pass")
    for pdf in tqdm(pdf_paths, desc="Extract PDFs"):
        try:
            folder, md = extract_pdf_to_md_enhanced(pdf, OUTPUT_DIR)
            processed.append((pdf, folder, md))
        except Exception as e:
            logging.exception(f"[ERROR] failed extract {pdf}: {e}")
            # continue to next PDF

    md_paths = [md for _, _, md in processed]
    chunks, chunk_meta = build_chunks_per_doc(md_paths, chunk_sent_count=3)
    log(f"[INDEX] Built {len(chunks)} chunks from {len(md_paths)} docs")

    log("[INDEX] Preparing retrievers (TF-IDF, BM25, semantic embeddings, reranker)")
    try:
        retrievers = prepare_retrievers(chunks)
    except Exception as e:
        logging.exception(f"[ERROR] prepare_retrievers failed: {e}")
        return

    question_csv = os.path.join(INPUT_DIR, "question.csv")
    if not os.path.exists(question_csv):
        matches = glob.glob(os.path.join(INPUT_DIR, "**", "question.csv"), recursive=True)
        question_csv = matches[0] if matches else None
    if not question_csv:
        log("[ERROR] question.csv not found.", logging.ERROR)
        return

    df_q = pd.read_csv(question_csv)
    answers = []
    per_question_logs = []

    for idx, row in tqdm(df_q.iterrows(), total=len(df_q), desc="Answering Qs"):
        qid = int(idx) + 1
        qtext = safe_text(row.get("Question", ""))
        try:
            log(f"[QA] Q{qid}: {qtext}")
            chosen, details = hybrid_retrieve_and_answer(row, retrievers, chunks, chunk_meta, topk=8)

            # ensure chosen is list-like, fallback if unexpected
            if not chosen or not isinstance(chosen, (list, tuple)):
                chosen = ["A"]

            answers.append(chosen)

            scores = details.get("option_final_scores", []) if isinstance(details, dict) else []
            for i, sc in enumerate(scores):
                log(f"   Option {chr(65+i)} score={sc:.4f}")
            log(f"   => chosen: {chosen}")

            per_question_logs.append({
                "qid": qid,
                "question": qtext,
                "chosen": chosen,
                "scores": scores,
                "details": details.get("per_option_details", []) if isinstance(details, dict) else []
            })

        except Exception as e:
            # log full traceback to pipeline.log
            logging.exception(f"[ERROR] Failed Q{qid}: {e}")

            # append fallback answer so we always keep correct count
            fallback = ["A"]
            answers.append(fallback)

            per_question_logs.append({
                "qid": qid,
                "question": qtext,
                "chosen": fallback,
                "error": str(e)
            })
            # continue to next question

    # Ensure answers length matches number of questions BEFORE writing answer.md
    if len(answers) != len(df_q):
        log(f"[WARN] Expected {len(df_q)} answers, got {len(answers)} — filling missing with default.", logging.WARNING)
        while len(answers) < len(df_q):
            answers.append(["A"])

    # Now build and write the answer.md (after we've ensured correct count)
    answer_path = build_answer_md(OUTPUT_DIR, processed, df_q, answers)

    log(f"[DONE] Pipeline finished in {time.time() - t0:.1f}s. Answer file at {answer_path}")

    # write per-question logs with details
    try:
        with open(os.path.join(OUTPUT_DIR, "per_question_logs.json"), "w", encoding="utf-8") as fh:
            json.dump(per_question_logs, fh, ensure_ascii=False, indent=2)
    except Exception as e:
        logging.exception(f"[ERROR] Failed writing per_question_logs.json: {e}")

if __name__ == "__main__":
    main() 
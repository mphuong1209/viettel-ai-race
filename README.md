# 🧠 Viettel AI Race - DUDUBUBUBU 🧩  
## 📄 Văn bản kỹ thuật (Extraction + QA Pipeline)

---

## 📘 Bối cảnh & Bài toán

**Bối cảnh:** Cuộc thi Viettel AI Race đặt ra thử thách xây dựng một hệ thống AI có khả năng tự động đọc hiểu, trích xuất thông tin từ các tài liệu kỹ thuật phức tạp (dạng PDF chứa văn bản, bảng biểu, hình ảnh) và trả lời chính xác các câu hỏi trắc nghiệm dựa trên nội dung đó.

**Mô tả giải pháp:**
Pipeline xử lý tự động **trích xuất nội dung PDF kỹ thuật và trả lời câu hỏi (QA)** bao gồm:
1. **Extraction**: đọc PDF, tách tiêu đề, bảng, hình ảnh → lưu thành Markdown.  
2. **QA**: đọc `question.csv`, kết hợp TF-IDF + BM25 + Semantic Embedding + CrossEncoder để tìm và chọn đáp án đúng.

Tất cả được tích hợp trong **`main.py`**, chạy end-to-end từ PDF đầu vào đến file kết quả `answer.md`.

---

## 📂 Cấu trúc thư mục

```text
Viettel AI Race - DUDUBUBUBU/
│
├── main.py                     # Pipeline chính (chứa toàn bộ logic Extract + QA)
├── requirements.txt            # Danh sách thư viện và công nghệ cần cài đặt
│
├── input/                      # 📥 Thư mục chứa dữ liệu đầu vào (Cần chuẩn bị trước)
│   ├── question.csv            # File danh sách câu hỏi trắc nghiệm
│   ├── Public427.pdf           # Các file PDF kỹ thuật cần đọc hiểu
│   ├── Public428.pdf
│   ├── ...
│   └── Public675.pdf
│
└── submissions/                # 📤 Thư mục chứa kết quả đầu ra (Tự động sinh ra)
    ├── Public_427/
    │   ├── main.md             # Nội dung text và bảng biểu dạng Markdown của PDF 427
    │   └── images/             # Thư mục chứa các hình ảnh cắt ra từ PDF 427
    │       ├── image_1.png
    │       └── ...
    ├── Public_428/
    │   ├── main.md
    │   └── images/
    ├── ...
    ├── Public_675/
    │   ├── main.md
    │   └── images/
    │
    ├── answer.md               # File kết quả QA tổng hợp để nộp bài
    ├── pipeline.log            # File log ghi lại tiến trình và lỗi chạy hệ thống
    └── per_question_logs.json  # Ghi chú chi tiết điểm số Reranker của từng câu hỏi
```

---

## 🛠️ Các hàm và luồng xử lý chính

Hệ thống được chia thành các hàm/module cốt lõi trong `main.py` như sau:

- **`process_pdf(pdf_path)`**: Module chịu trách nhiệm đọc PDF, phát hiện layout và phân loại vùng dữ liệu (text, table, image).
- **`extract_tables(pdf_page)`**: Sử dụng `pdfplumber` / `camelot` để nhận diện cấu trúc bảng và chuyển đổi sang định dạng HTML (được nhúng thẳng vào Markdown).
- **`embed_text(text_chunks)`**: Sử dụng mô hình Multilingual E5 để mã hoá các đoạn văn bản trích xuất được thành các vector ngữ nghĩa (embeddings).
- **`hybrid_retrieve(question, context_chunks)`**: Kết hợp tìm kiếm từ khoá (TF-IDF, BM25) và tìm kiếm ngữ nghĩa (Semantic Search) để thu thập Top-K đoạn văn bản chứa thông tin tiềm năng nhất.
- **`rerank_candidates(question, candidates)`**: Sử dụng mô hình Cross-Encoder (MS-MARCO) để chấm điểm lại mức độ phù hợp giữa câu hỏi và các đoạn ngữ cảnh, từ đó suy luận ra đáp án đúng cuối cùng.

---

## ⚙️ Cài đặt môi trường

### 1️⃣ Tạo và kích hoạt môi trường ảo
```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
# hoặc
source .venv/bin/activate  # Linux / macOS
```

### 2️⃣ Cài đặt thư viện
```bash
pip install -r requirements.txt
```

---

## 📦 File `requirements.txt`

```text
# === Core NLP and Embedding ===
sentence-transformers==2.7.0
transformers==4.44.2
torch==2.2.2
numpy==1.26.4
scikit-learn==1.4.2
scipy==1.12.0

# === Text retrieval and BM25 ===
rank-bm25==0.2.2

# === PDF extraction & parsing ===
pdfplumber==0.11.3
PyMuPDF==1.24.3
camelot-py==0.11.0
pdfminer.six==20231228

# === Text / HTML / Markdown ===
beautifulsoup4==4.12.3
markdownify==0.13.1

# === Progress bar / Logging / System ===
tqdm==4.66.4
loguru==0.7.2
colorama==0.4.6

# === Pandas for CSV (questions file) ===
pandas==2.2.2

# === Optional (used for structured saving and JSON logs) ===
orjson==3.10.3

# === Utilities for environment / configs ===
python-dotenv==1.0.1
```

---

## 🚀 Cách chạy pipeline

```bash
python main.py
```

Sau khi chạy, toàn bộ output sẽ nằm trong thư mục `submissions/`.

---

## 📄 Output chính

| File / Folder | Mô tả |
|----------------|-------|
| `submissions/<PDF_NAME>/main.md` | Markdown nội dung trích từ PDF |
| `submissions/<PDF_NAME>/images/` | Ảnh trích từ PDF |
| `submissions/answer.md` | Kết quả QA theo định dạng `num_correct,answers` |
| `submissions/pipeline.log` | Nhật ký xử lý |
| `submissions/per_question_logs.json` | Chi tiết từng câu hỏi và điểm reranker |

---

## 🧠 Công nghệ và Mô hình sử dụng

Dự án sử dụng các công nghệ và thư viện Deep Learning/NLP tiên tiến để giải quyết bài toán:

### 1. Công nghệ Lõi (Core Technologies)
- **PyTorch & Transformers (HuggingFace)**: Framework Deep Learning chính để chạy các mô hình ngôn ngữ (Embedding, Reranker).
- **Sentence-Transformers**: Thư viện hỗ trợ khởi tạo và inference các mô hình Semantic Search đa ngôn ngữ hiệu quả.
- **Scikit-learn & Rank-BM25**: Xử lý thuật toán tìm kiếm truyền thống dựa trên tần suất từ vựng (Lexical Search).

### 2. Công nghệ Xử lý PDF (PDF Parsers)
- **PyMuPDF (fitz)**: Đọc nhanh cấu trúc text và toạ độ hình ảnh trong file PDF.
- **pdfplumber & camelot-py**: Xử lý chuyên sâu việc nhận diện lưới (grid) của các bảng biểu phức tạp.
- **BeautifulSoup4 & Markdownify**: Làm sạch mã HTML của bảng biểu và chuyển đổi mượt mà sang định dạng Markdown.

### 3. Mô hình AI (AI Models)
| Loại | Model | Mục đích |
|------|--------|----------|
| **Embedding** | `intfloat/multilingual-e5-small` | Mã hoá câu hỏi và văn bản thành vector (hỗ trợ tốt đa ngôn ngữ, tiếng Việt). |
| **Reranker** | `cross-encoder/ms-marco-MiniLM-L-6-v2` | Chấm điểm và xếp hạng lại (Reranking) độ phù hợp giữa câu hỏi và đoạn văn bản. |
| **TF-IDF** | `sklearn` | Truy xuất ngữ cảnh cơ bản dựa trên từ khoá. |
| **BM25** | `rank-bm25` | Thuật toán tìm kiếm có trọng số, bù đắp hiệu quả cho semantic search. |

---

## 💡 Ghi chú
- Thiết bị mặc định: `cpu`. Nếu có GPU → sửa trong `main.py`:
  ```python
  DEVICE = "cuda"
  ```
- Pipeline tương thích với nhiều file PDF trong cùng thư mục `input/`.
- Hỗ trợ markdown rõ ràng, giữ nguyên bảng (HTML table block), hình ảnh, và caption.

---

## ✅ Ví dụ đầu ra `answer.md`

```text
### TASK EXTRACT
# Public427
<markdown content>

### TASK QA
num_correct,answers
1,A
2,"A,B"
3,"A,B,C"
```

---

**📌 Tác giả:** Đội DUDUBUBUBU — Viettel AI Race 2025  
**📅 Phiên bản:** Final Submission — Technical Document Extraction + QA

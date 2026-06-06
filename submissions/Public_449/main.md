# Public_449

<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Module</th><th>Loại log</th><th>Mức độ</th><th></th><th>Hành</th><th></th><th>Mô tả chi tiết</th><th>Kết quả</th><th>Ghi chú</th></tr></thead><tbody><tr><td></td><td></td><td></td><td></td><td>động</td><td></td><td></td><td></td><td></td></tr><tr><td>RPA</td><td>TransactionLog</td><td>Critical</td><td>Xuất
log</td><td></td><td></td><td>Hệ thống RPA
Xuất log loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>CRM</td><td>TransactionLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td></td><td></td><td>Hệ thống CRM
Nén và lưu trữ log
loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Billing</td><td>PerformanceLog</td><td>Error</td><td>Phân
tích
log</td><td></td><td></td><td>Hệ thống Billing
Phân tích log loại
PerformanceLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Có dashboard
Grafana</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Critical</td><td>Xóa
log</td><td></td><td></td><td>Hệ thống Infra Xóa
log loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>QA</td><td>AuditLog</td><td>Warning</td><td>Xuất</td><td></td><td></td><td>Hệ thống QA Xuất</td><td>Không</td><td>Có dashboard</td></tr></tbody></table>

|<image_1>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log</th><th>log loại AuditLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th>mất mát
dữ liệu</th><th>Grafana</th></tr></thead><tbody><tr><td>IPCC</td><td>PerformanceLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống IPCC
Nén và lưu trữ log
loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Có dashboard
Grafana</td></tr><tr><td>IPCC</td><td>ErrorLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống IPCC
Xóa log loại
ErrorLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Có dashboard
Grafana</td></tr><tr><td>Billing</td><td>ErrorLog</td><td>Warning</td><td>Xóa
log</td><td>Hệ thống Billing
Xóa log loại
ErrorLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>AuditLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống CRM
Gửi log sang SIEM
loại AuditLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Infra</td><td>AuditLog</td><td>Error</td><td>Gửi
log</td><td>Hệ thống Infra Gửi
log sang SIEM loại</td><td>Không
mất mát</td><td>Theo chuẩn
syslog</td></tr></tbody></table>

|<image_2>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>sang
SIEM</th><th>AuditLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</th><th>dữ liệu</th><th>RFC5424</th></tr></thead><tbody><tr><td>RPA</td><td>PerformanceLog</td><td>Fatal</td><td>Xuất
log</td><td>Hệ thống RPA
Xuất log loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>QA</td><td>AccessLog</td><td>Info</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống QA Nén
và lưu trữ log loại
AccessLog với
mức Info, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Billing</td><td>ErrorLog</td><td>Info</td><td>Xuất
log</td><td>Hệ thống Billing
Xuất log loại
ErrorLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Phân quyền chi
tiết</td></tr><tr><td>IVR</td><td>TransactionLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống IVR Xóa
log loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Phân quyền chi
tiết</td></tr><tr><td>IVR</td><td>PerformanceLog</td><td>Error</td><td>Xóa
log</td><td>Hệ thống IVR Xóa
log loại
PerformanceLog</td><td>Có chỉ
số
thống</td><td>Gửi log sang
ELK</td></tr></tbody></table>

|<image_3>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</th><th>kê</th><th></th></tr></thead><tbody><tr><td>IPCC</td><td>AuditLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống IPCC
Nén và lưu trữ log
loại AuditLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Infra</td><td>AccessLog</td><td>Warning</td><td>Xuất
log</td><td>Hệ thống Infra
Xuất log loại
AccessLog với
mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>QA</td><td>AccessLog</td><td>Warning</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống QA Nén
và lưu trữ log loại
AccessLog với
mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Phân quyền chi
tiết</td></tr><tr><td>Infra</td><td>ErrorLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống Infra
Xuất log loại
ErrorLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Gửi log sang
ELK</td></tr><tr><td>QA</td><td>AuditLog</td><td>Error</td><td>Xóa
log</td><td>Hệ thống QA Xóa
log loại AuditLog
với mức Error, dữ
liệu lưu trữ tối</td><td>Tích
hợp
cảnh
báo</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_4>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>thiểu 90 ngày.</th><th>realtime</th><th></th></tr></thead><tbody><tr><td>CRM</td><td>AuditLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống CRM
Xóa log loại
AuditLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Phân quyền chi
tiết</td></tr><tr><td>CRM</td><td>PerformanceLog</td><td>Warning</td><td>Xuất
log</td><td>Hệ thống CRM
Xuất log loại
PerformanceLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống Infra
Xuất log loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IPCC</td><td>TransactionLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống IPCC
Nén và lưu trữ log
loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Phân quyền chi
tiết</td></tr><tr><td>IPCC</td><td>PerformanceLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống IPCC
Xóa log loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối</td><td>Có chỉ
số
thống
kê</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_5>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>thiểu 90 ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>Billing</td><td>AccessLog</td><td>Fatal</td><td>Phân
tích
log</td><td>Hệ thống Billing
Phân tích log loại
AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>RPA</td><td>ErrorLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống RPA Xóa
log loại ErrorLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Có dashboard
Grafana</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Info</td><td>Xuất
log</td><td>Hệ thống Infra
Xuất log loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>IVR</td><td>ErrorLog</td><td>Warning</td><td>Xuất
log</td><td>Hệ thống IVR Xuất
log loại ErrorLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Có dashboard
Grafana</td></tr><tr><td>QA</td><td>AuditLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống QA Gửi
log sang SIEM loại
AuditLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Infra</td><td>PerformanceLog</td><td>Critical</td><td>Phân</td><td>Hệ thống Infra</td><td>Có chỉ</td><td>Theo chuẩn</td></tr></tbody></table>

|<image_6>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>tích
log</th><th>Phân tích log loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th>số
thống
kê</th><th>syslog
RFC5424</th></tr></thead><tbody><tr><td>QA</td><td>AuditLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống QA Xuất
log loại AuditLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>IPCC</td><td>TransactionLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống IPCC
Nén và lưu trữ log
loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Gửi log sang
ELK</td></tr><tr><td>RPA</td><td>PerformanceLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống RPA
Phân tích log loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Có dashboard
Grafana</td></tr><tr><td>Infra</td><td>AuditLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại AuditLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Có dashboard
Grafana</td></tr><tr><td>RPA</td><td>ErrorLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống RPA Xóa
log loại ErrorLog
với mức Fatal, dữ</td><td>Tích
hợp
cảnh</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_7>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>liệu lưu trữ tối
thiểu 90 ngày.</th><th>báo
realtime</th><th></th></tr></thead><tbody><tr><td>Billing</td><td>ErrorLog</td><td>Info</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Billing
Gửi log sang SIEM
loại ErrorLog với
mức Info, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Phân quyền chi
tiết</td></tr><tr><td>CRM</td><td>PerformanceLog</td><td>Critical</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống CRM
Gửi log sang SIEM
loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>Billing</td><td>TransactionLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>CRM</td><td>TransactionLog</td><td>Error</td><td>Phân
tích
log</td><td>Hệ thống CRM
Phân tích log loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>IVR</td><td>AuditLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống IVR Xuất
log loại AuditLog
với mức Critical,</td><td>Không
mất mát</td><td>Gửi log sang
ELK</td></tr></tbody></table>

|<image_8>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th>dữ liệu</th><th></th></tr></thead><tbody><tr><td>CRM</td><td>ErrorLog</td><td>Info</td><td>Xuất
log</td><td>Hệ thống CRM
Xuất log loại
ErrorLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IPCC</td><td>ErrorLog</td><td>Fatal</td><td>Phân
tích
log</td><td>Hệ thống IPCC
Phân tích log loại
ErrorLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>QA</td><td>AuditLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống QA Nén
và lưu trữ log loại
AuditLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>TransactionLog</td><td>Critical</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống CRM
Gửi log sang SIEM
loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Infra</td><td>ErrorLog</td><td>Warning</td><td>Nén
và
lưu
trữ</td><td>Hệ thống Infra Nén
và lưu trữ log loại
ErrorLog với mức
Warning, dữ liệu</td><td>Log
được
mã hóa
AES-</td><td>Theo chuẩn
syslog
RFC5424</td></tr></tbody></table>

|<image_9>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log</th><th>lưu trữ tối thiểu 90
ngày.</th><th>256</th><th></th></tr></thead><tbody><tr><td>RPA</td><td>TransactionLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống RPA Gửi
log sang SIEM loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>QA</td><td>ErrorLog</td><td>Error</td><td>Xuất
log</td><td>Hệ thống QA Xuất
log loại ErrorLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Gửi log sang
ELK</td></tr><tr><td>QA</td><td>AccessLog</td><td>Info</td><td>Xuất
log</td><td>Hệ thống QA Xuất
log loại AccessLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Phân quyền chi
tiết</td></tr><tr><td>CRM</td><td>AccessLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống CRM
Gửi log sang SIEM
loại AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Billing</td><td>PerformanceLog</td><td>Warning</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại
PerformanceLog
với mức Warning,
dữ liệu lưu trữ tối</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Có dashboard
Grafana</td></tr></tbody></table>

|<image_10>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>thiểu 90 ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>IPCC</td><td>AccessLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IPCC
Gửi log sang SIEM
loại AccessLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Có dashboard
Grafana</td></tr><tr><td>Billing</td><td>AuditLog</td><td>Warning</td><td>Xuất
log</td><td>Hệ thống Billing
Xuất log loại
AuditLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Có dashboard
Grafana</td></tr><tr><td>Billing</td><td>AuditLog</td><td>Error</td><td>Xuất
log</td><td>Hệ thống Billing
Xuất log loại
AuditLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Billing</td><td>AccessLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>AccessLog</td><td>Warning</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống CRM
Nén và lưu trữ log
loại AccessLog với
mức Warning, dữ
liệu lưu trữ tối</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr></tbody></table>

|<image_11>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>thiểu 90 ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>Infra</td><td>AccessLog</td><td>Fatal</td><td>Phân
tích
log</td><td>Hệ thống Infra
Phân tích log loại
AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Có dashboard
Grafana</td></tr><tr><td>IPCC</td><td>TransactionLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống IPCC
Xóa log loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>QA</td><td>AccessLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống QA Nén
và lưu trữ log loại
AccessLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Có dashboard
Grafana</td></tr><tr><td>IPCC</td><td>ErrorLog</td><td>Error</td><td>Phân
tích
log</td><td>Hệ thống IPCC
Phân tích log loại
ErrorLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Gửi log sang
ELK</td></tr><tr><td>Infra</td><td>ErrorLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống Infra
Phân tích log loại
ErrorLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90</td><td>Không
mất mát
dữ liệu</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_12>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>IVR</td><td>AccessLog</td><td>Warning</td><td>Phân
tích
log</td><td>Hệ thống IVR
Phân tích log loại
AccessLog với
mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Có dashboard
Grafana</td></tr><tr><td>IVR</td><td>TransactionLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống IVR Nén
và lưu trữ log loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>QA</td><td>ErrorLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống QA Gửi
log sang SIEM loại
ErrorLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>RPA</td><td>TransactionLog</td><td>Fatal</td><td>Phân
tích
log</td><td>Hệ thống RPA
Phân tích log loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Billing</td><td>AccessLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Billing
Gửi log sang SIEM
loại AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr></tbody></table>

|<image_13>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>CRM</td><td>TransactionLog</td><td>Info</td><td>Phân
tích
log</td><td>Hệ thống CRM
Phân tích log loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>Billing</td><td>ErrorLog</td><td>Info</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại ErrorLog với
mức Info, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>RPA</td><td>TransactionLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống RPA Nén
và lưu trữ log loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Gửi log sang
ELK</td></tr><tr><td>Infra</td><td>ErrorLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại ErrorLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Có dashboard
Grafana</td></tr><tr><td>IVR</td><td>ErrorLog</td><td>Info</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống IVR Nén
và lưu trữ log loại
ErrorLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Theo chuẩn
syslog
RFC5424</td></tr></tbody></table>

|<image_14>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>IPCC</th><th>AuditLog</th><th>Error</th><th>Gửi
log
sang
SIEM</th><th>Hệ thống IPCC
Gửi log sang SIEM
loại AuditLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90
ngày.</th><th>Tích
hợp
cảnh
báo
realtime</th><th>Phân quyền chi
tiết</th></tr></thead><tbody><tr><td>QA</td><td>TransactionLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống QA Gửi
log sang SIEM loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>Infra</td><td>AuditLog</td><td>Warning</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại AuditLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>IVR</td><td>ErrorLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IVR Gửi
log sang SIEM loại
ErrorLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>IVR</td><td>AuditLog</td><td>Fatal</td><td>Xuất
log</td><td>Hệ thống IVR Xuất
log loại AuditLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Có dashboard
Grafana</td></tr><tr><td>Infra</td><td>PerformanceLog</td><td>Info</td><td>Nén
và
lưu</td><td>Hệ thống Infra Nén
và lưu trữ log loại
PerformanceLog</td><td>Không
mất mát</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_15>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>trữ
log</th><th>với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</th><th>dữ liệu</th><th></th></tr></thead><tbody><tr><td>Billing</td><td>PerformanceLog</td><td>Error</td><td>Xuất
log</td><td>Hệ thống Billing
Xuất log loại
PerformanceLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>CRM</td><td>TransactionLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống CRM
Nén và lưu trữ log
loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>QA</td><td>TransactionLog</td><td>Fatal</td><td>Xuất
log</td><td>Hệ thống QA Xuất
log loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Phân quyền chi
tiết</td></tr><tr><td>RPA</td><td>TransactionLog</td><td>Critical</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống RPA Gửi
log sang SIEM loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>QA</td><td>TransactionLog</td><td>Critical</td><td>Phân
tích</td><td>Hệ thống QA Phân
tích log loại
TransactionLog</td><td>Có chỉ
số
thống</td><td>Theo chuẩn
syslog</td></tr></tbody></table>

|<image_16>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log</th><th>với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th>kê</th><th>RFC5424</th></tr></thead><tbody><tr><td>CRM</td><td>AccessLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống CRM
Gửi log sang SIEM
loại AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Billing</td><td>PerformanceLog</td><td>Critical</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Phân quyền chi
tiết</td></tr><tr><td>QA</td><td>TransactionLog</td><td>Error</td><td>Xuất
log</td><td>Hệ thống QA Xuất
log loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>Billing</td><td>AccessLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống Billing
Xóa log loại
AccessLog với
mức Info, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Có dashboard
Grafana</td></tr><tr><td>CRM</td><td>AuditLog</td><td>Warning</td><td>Nén
và
lưu</td><td>Hệ thống CRM
Nén và lưu trữ log
loại AuditLog với</td><td>Có chỉ
số
thống</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_17>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>trữ
log</th><th>mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</th><th>kê</th><th></th></tr></thead><tbody><tr><td>Billing</td><td>AccessLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống Billing
Xóa log loại
AccessLog với
mức Info, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IVR</td><td>AccessLog</td><td>Error</td><td>Xóa
log</td><td>Hệ thống IVR Xóa
log loại AccessLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IVR</td><td>AccessLog</td><td>Error</td><td>Xóa
log</td><td>Hệ thống IVR Xóa
log loại AccessLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Gửi log sang
ELK</td></tr><tr><td>Billing</td><td>TransactionLog</td><td>Info</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Gửi log sang
ELK</td></tr><tr><td>Billing</td><td>TransactionLog</td><td>Error</td><td>Xóa
log</td><td>Hệ thống Billing
Xóa log loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối</td><td>Log
được
mã hóa
AES-</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_18>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>thiểu 90 ngày.</th><th>256</th><th></th></tr></thead><tbody><tr><td>Infra</td><td>AccessLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại AccessLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>RPA</td><td>ErrorLog</td><td>Critical</td><td>Xóa
log</td><td>Hệ thống RPA Xóa
log loại ErrorLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>Billing</td><td>TransactionLog</td><td>Warning</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại
TransactionLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Infra</td><td>PerformanceLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Infra Gửi
log sang SIEM loại
TransactionLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_19>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>IPCC</th><th>PerformanceLog</th><th>Critical</th><th>Nén
và
lưu
trữ
log</th><th>Hệ thống IPCC
Nén và lưu trữ log
loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th>Tích
hợp
cảnh
báo
realtime</th><th>Phân quyền chi
tiết</th></tr></thead><tbody><tr><td>IPCC</td><td>TransactionLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IPCC
Gửi log sang SIEM
loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Có dashboard
Grafana</td></tr><tr><td>RPA</td><td>AccessLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống RPA Gửi
log sang SIEM loại
AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>IVR</td><td>AccessLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống IVR
Phân tích log loại
AccessLog với
mức Critical, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Phân quyền chi
tiết</td></tr><tr><td>Billing</td><td>AuditLog</td><td>Critical</td><td>Xóa
log</td><td>Hệ thống Billing
Xóa log loại
AuditLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr></tbody></table>

|<image_20>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>QA</td><td>AccessLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống QA Gửi
log sang SIEM loại
AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Có dashboard
Grafana</td></tr><tr><td>Billing</td><td>TransactionLog</td><td>Info</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Billing
Gửi log sang SIEM
loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Billing</td><td>AccessLog</td><td>Warning</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại AccessLog với
mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Phân quyền chi
tiết</td></tr><tr><td>IPCC</td><td>ErrorLog</td><td>Error</td><td>Xóa
log</td><td>Hệ thống IPCC
Xóa log loại
ErrorLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>RPA</td><td>TransactionLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống RPA
Phân tích log loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối</td><td>Có thể
truy
xuất khi
cần</td><td>Gửi log sang
ELK</td></tr></tbody></table>

|<image_21>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>thiểu 90 ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>Billing</td><td>AuditLog</td><td>Error</td><td>Phân
tích
log</td><td>Hệ thống Billing
Phân tích log loại
AuditLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Phân quyền chi
tiết</td></tr><tr><td>QA</td><td>TransactionLog</td><td>Info</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống QA Nén
và lưu trữ log loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>AuditLog</td><td>Info</td><td>Phân
tích
log</td><td>Hệ thống CRM
Phân tích log loại
AuditLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>QA</td><td>TransactionLog</td><td>Warning</td><td>Phân
tích
log</td><td>Hệ thống QA Phân
tích log loại
TransactionLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Phân quyền chi
tiết</td></tr><tr><td>Billing</td><td>TransactionLog</td><td>Fatal</td><td>Xuất
log</td><td>Hệ thống Billing
Xuất log loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Gửi log sang
ELK</td></tr></tbody></table>

|<image_22>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>thiểu 90 ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>Infra</td><td>AccessLog</td><td>Warning</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại AccessLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Billing</td><td>TransactionLog</td><td>Info</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Billing
Gửi log sang SIEM
loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Phân quyền chi
tiết</td></tr><tr><td>CRM</td><td>AccessLog</td><td>Critical</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống CRM
Nén và lưu trữ log
loại AccessLog với
mức Critical, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>QA</td><td>ErrorLog</td><td>Warning</td><td>Xóa
log</td><td>Hệ thống QA Xóa
log loại ErrorLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Infra Nén
và lưu trữ log loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr></tbody></table>

|<image_23>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>IPCC</th><th>AuditLog</th><th>Error</th><th>Nén
và
lưu
trữ
log</th><th>Hệ thống IPCC
Nén và lưu trữ log
loại AuditLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90
ngày.</th><th>Có thể
truy
xuất khi
cần</th><th>Gửi log sang
ELK</th></tr></thead><tbody><tr><td>QA</td><td>AccessLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống QA Nén
và lưu trữ log loại
AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>CRM</td><td>PerformanceLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống CRM
Gửi log sang SIEM
loại
PerformanceLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>RPA</td><td>TransactionLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống RPA Nén
và lưu trữ log loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Có dashboard
Grafana</td></tr><tr><td>CRM</td><td>AuditLog</td><td>Warning</td><td>Phân
tích
log</td><td>Hệ thống CRM
Phân tích log loại
AuditLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Tự động xóa
log sau 180
ngày</td></tr></tbody></table>

|<image_24>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Infra</th><th>ErrorLog</th><th>Critical</th><th>Nén
và
lưu
trữ
log</th><th>Hệ thống Infra Nén
và lưu trữ log loại
ErrorLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</th><th>Không
mất mát
dữ liệu</th><th>Gửi log sang
ELK</th></tr></thead><tbody><tr><td>RPA</td><td>PerformanceLog</td><td>Critical</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống RPA Nén
và lưu trữ log loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Có dashboard
Grafana</td></tr><tr><td>IPCC</td><td>AuditLog</td><td>Warning</td><td>Phân
tích
log</td><td>Hệ thống IPCC
Phân tích log loại
AuditLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Billing</td><td>AccessLog</td><td>Info</td><td>Xuất
log</td><td>Hệ thống Billing
Xuất log loại
AccessLog với
mức Info, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Billing</td><td>AccessLog</td><td>Warning</td><td>Xuất
log</td><td>Hệ thống Billing
Xuất log loại
AccessLog với
mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Theo chuẩn
syslog
RFC5424</td></tr></tbody></table>

|<image_25>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>QA</th><th>TransactionLog</th><th>Warning</th><th>Xuất
log</th><th>Hệ thống QA Xuất
log loại
TransactionLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th>Có chỉ
số
thống
kê</th><th>Tự động xóa
log sau 180
ngày</th></tr></thead><tbody><tr><td>IVR</td><td>AccessLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IVR Gửi
log sang SIEM loại
AccessLog với
mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Phân quyền chi
tiết</td></tr><tr><td>IVR</td><td>ErrorLog</td><td>Warning</td><td>Xóa
log</td><td>Hệ thống IVR Xóa
log loại ErrorLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IPCC</td><td>AuditLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống IPCC
Xóa log loại
AuditLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Infra Nén
và lưu trữ log loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Phân quyền chi
tiết</td></tr><tr><td>Infra</td><td>AuditLog</td><td>Error</td><td>Nén
và</td><td>Hệ thống Infra Nén
và lưu trữ log loại</td><td>Tích
hợp</td><td>Theo chuẩn
syslog</td></tr></tbody></table>

|<image_26>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>lưu
trữ
log</th><th>AuditLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</th><th>cảnh
báo
realtime</th><th>RFC5424</th></tr></thead><tbody><tr><td>IPCC</td><td>PerformanceLog</td><td>Critical</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IPCC
Gửi log sang SIEM
loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Infra</td><td>PerformanceLog</td><td>Warning</td><td>Phân
tích
log</td><td>Hệ thống Infra
Phân tích log loại
PerformanceLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Infra</td><td>AccessLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại AccessLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>QA</td><td>PerformanceLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống QA Phân
tích log loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Infra</td><td>PerformanceLog</td><td>Critical</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại
PerformanceLog</td><td>Có thể
truy
xuất khi</td><td>Theo chuẩn
syslog</td></tr></tbody></table>

|<image_27>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th>cần</th><th>RFC5424</th></tr></thead><tbody><tr><td>QA</td><td>PerformanceLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống QA Nén
và lưu trữ log loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>RPA</td><td>ErrorLog</td><td>Warning</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống RPA Nén
và lưu trữ log loại
ErrorLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IPCC</td><td>ErrorLog</td><td>Critical</td><td>Xóa
log</td><td>Hệ thống IPCC
Xóa log loại
ErrorLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Phân quyền chi
tiết</td></tr><tr><td>QA</td><td>AccessLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống QA Xóa
log loại AccessLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>RPA</td><td>AuditLog</td><td>Warning</td><td>Nén
và
lưu
trữ</td><td>Hệ thống RPA Nén
và lưu trữ log loại
AuditLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90</td><td>Log
được
mã hóa
AES-</td><td>Theo chuẩn
syslog
RFC5424</td></tr></tbody></table>

|<image_28>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log</th><th>ngày.</th><th>256</th><th></th></tr></thead><tbody><tr><td>QA</td><td>AuditLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống QA Gửi
log sang SIEM loại
AuditLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>CRM</td><td>PerformanceLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống CRM
Gửi log sang SIEM
loại
PerformanceLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>RPA</td><td>TransactionLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống RPA Gửi
log sang SIEM loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Billing</td><td>AuditLog</td><td>Warning</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại AuditLog với
mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IPCC</td><td>AuditLog</td><td>Error</td><td>Nén
và
lưu
trữ</td><td>Hệ thống IPCC
Nén và lưu trữ log
loại AuditLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90</td><td>Log
được
mã hóa
AES-</td><td>Gửi log sang
ELK</td></tr></tbody></table>

|<image_29>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log</th><th>ngày.</th><th>256</th><th></th></tr></thead><tbody><tr><td>IPCC</td><td>PerformanceLog</td><td>Warning</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống IPCC
Nén và lưu trữ log
loại
PerformanceLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Có dashboard
Grafana</td></tr><tr><td>IPCC</td><td>TransactionLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IPCC
Gửi log sang SIEM
loại
TransactionLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>IVR</td><td>PerformanceLog</td><td>Warning</td><td>Phân
tích
log</td><td>Hệ thống IVR
Phân tích log loại
PerformanceLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Có dashboard
Grafana</td></tr><tr><td>Infra</td><td>AccessLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống Infra
Phân tích log loại
AccessLog với
mức Critical, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Billing</td><td>PerformanceLog</td><td>Warning</td><td>Nén
và
lưu
trữ</td><td>Hệ thống Billing
Nén và lưu trữ log
loại
PerformanceLog</td><td>Có thể
truy
xuất khi</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_30>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log</th><th>với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th>cần</th><th></th></tr></thead><tbody><tr><td>QA</td><td>AccessLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống QA Gửi
log sang SIEM loại
AccessLog với
mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>QA</td><td>PerformanceLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống QA Gửi
log sang SIEM loại
PerformanceLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Có dashboard
Grafana</td></tr><tr><td>IPCC</td><td>PerformanceLog</td><td>Fatal</td><td>Xuất
log</td><td>Hệ thống IPCC
Xuất log loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Infra</td><td>AccessLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Infra Gửi
log sang SIEM loại
AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>IPCC</td><td>ErrorLog</td><td>Error</td><td>Gửi
log
sang</td><td>Hệ thống IPCC
Gửi log sang SIEM
loại ErrorLog với
mức Error, dữ liệu</td><td>Có thể
truy
xuất khi</td><td>Tự động xóa
log sau 180
ngày</td></tr></tbody></table>

|<image_31>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>SIEM</th><th>lưu trữ tối thiểu 90
ngày.</th><th>cần</th><th></th></tr></thead><tbody><tr><td>IVR</td><td>AuditLog</td><td>Critical</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống IVR Nén
và lưu trữ log loại
AuditLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Có dashboard
Grafana</td></tr><tr><td>Billing</td><td>TransactionLog</td><td>Critical</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Billing
Gửi log sang SIEM
loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>RPA</td><td>PerformanceLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống RPA
Phân tích log loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>IPCC</td><td>AccessLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IPCC
Gửi log sang SIEM
loại AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Phân quyền chi
tiết</td></tr><tr><td>Infra</td><td>AuditLog</td><td>Critical</td><td>Nén
và
lưu
trữ</td><td>Hệ thống Infra Nén
và lưu trữ log loại
AuditLog với mức
Critical, dữ liệu lưu</td><td>Tích
hợp
cảnh
báo</td><td>Tự động xóa
log sau 180
ngày</td></tr></tbody></table>

|<image_32>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log</th><th>trữ tối thiểu 90
ngày.</th><th>realtime</th><th></th></tr></thead><tbody><tr><td>Billing</td><td>AccessLog</td><td>Error</td><td>Xóa
log</td><td>Hệ thống Billing
Xóa log loại
AccessLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Phân quyền chi
tiết</td></tr><tr><td>QA</td><td>AuditLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống QA Xuất
log loại AuditLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>QA</td><td>PerformanceLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống QA Gửi
log sang SIEM loại
PerformanceLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Phân quyền chi
tiết</td></tr><tr><td>Infra</td><td>ErrorLog</td><td>Error</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại ErrorLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>AccessLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống CRM
Xóa log loại
AccessLog với
mức Info, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr></tbody></table>

|<image_33>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>IPCC</th><th>AccessLog</th><th>Fatal</th><th>Gửi
log
sang
SIEM</th><th>Hệ thống IPCC
Gửi log sang SIEM
loại AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</th><th>Tích
hợp
cảnh
báo
realtime</th><th>Gửi log sang
ELK</th></tr></thead><tbody><tr><td>QA</td><td>AuditLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống QA Nén
và lưu trữ log loại
AuditLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>RPA</td><td>ErrorLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống RPA Xóa
log loại ErrorLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>CRM</td><td>TransactionLog</td><td>Info</td><td>Xuất
log</td><td>Hệ thống CRM
Xuất log loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>Infra</td><td>PerformanceLog</td><td>Info</td><td>Xuất
log</td><td>Hệ thống Infra
Xuất log loại
PerformanceLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Warning</td><td>Gửi
log</td><td>Hệ thống Infra Gửi
log sang SIEM loại</td><td>Tích
hợp</td><td>Theo chuẩn
syslog</td></tr></tbody></table>

|<image_34>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>sang
SIEM</th><th>TransactionLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th>cảnh
báo
realtime</th><th>RFC5424</th></tr></thead><tbody><tr><td>IVR</td><td>AuditLog</td><td>Warning</td><td>Xuất
log</td><td>Hệ thống IVR Xuất
log loại AuditLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Billing</td><td>ErrorLog</td><td>Warning</td><td>Xóa
log</td><td>Hệ thống Billing
Xóa log loại
ErrorLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Phân quyền chi
tiết</td></tr><tr><td>IPCC</td><td>PerformanceLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống IPCC
Phân tích log loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>RPA</td><td>ErrorLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống RPA Nén
và lưu trữ log loại
ErrorLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Gửi log sang
ELK</td></tr><tr><td>RPA</td><td>TransactionLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống RPA
Xuất log loại
TransactionLog
với mức Critical,</td><td>Không
mất mát
dữ liệu</td><td>Có dashboard
Grafana</td></tr></tbody></table>

|<image_35>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>RPA</td><td>AuditLog</td><td>Critical</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống RPA Nén
và lưu trữ log loại
AuditLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Phân quyền chi
tiết</td></tr><tr><td>QA</td><td>ErrorLog</td><td>Fatal</td><td>Phân
tích
log</td><td>Hệ thống QA Phân
tích log loại
ErrorLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Gửi log sang
ELK</td></tr><tr><td>RPA</td><td>TransactionLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống RPA Gửi
log sang SIEM loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>RPA</td><td>ErrorLog</td><td>Warning</td><td>Phân
tích
log</td><td>Hệ thống RPA
Phân tích log loại
ErrorLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>PerformanceLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống CRM
Xóa log loại
PerformanceLog
với mức Info, dữ
liệu lưu trữ tối</td><td>Có chỉ
số
thống
kê</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_36>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>thiểu 90 ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>Infra</td><td>AccessLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Infra Nén
và lưu trữ log loại
AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>IVR</td><td>ErrorLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống IVR
Phân tích log loại
ErrorLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Infra</td><td>PerformanceLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Infra Nén
và lưu trữ log loại
PerformanceLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>IPCC</td><td>TransactionLog</td><td>Info</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IPCC
Gửi log sang SIEM
loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Phân quyền chi
tiết</td></tr><tr><td>IPCC</td><td>ErrorLog</td><td>Error</td><td>Nén
và
lưu
trữ</td><td>Hệ thống IPCC
Nén và lưu trữ log
loại ErrorLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr></tbody></table>

|<image_37>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log</th><th>ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>RPA</td><td>PerformanceLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống RPA Gửi
log sang SIEM loại
PerformanceLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Infra</td><td>ErrorLog</td><td>Critical</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại ErrorLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Gửi log sang
ELK</td></tr><tr><td>IVR</td><td>PerformanceLog</td><td>Critical</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IVR Gửi
log sang SIEM loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Infra</td><td>AuditLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Infra Gửi
log sang SIEM loại
AuditLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>IVR</td><td>ErrorLog</td><td>Critical</td><td>Xóa
log</td><td>Hệ thống IVR Xóa
log loại ErrorLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Phân quyền chi
tiết</td></tr><tr><td>QA</td><td>PerformanceLog</td><td>Fatal</td><td>Nén</td><td>Hệ thống QA Nén</td><td>Có thể</td><td>Tự động xóa</td></tr></tbody></table>

|<image_38>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>và
lưu
trữ
log</th><th>và lưu trữ log loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</th><th>truy
xuất khi
cần</th><th>log sau 180
ngày</th></tr></thead><tbody><tr><td>RPA</td><td>TransactionLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống RPA
Phân tích log loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Gửi log sang
ELK</td></tr><tr><td>RPA</td><td>PerformanceLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống RPA Xóa
log loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Phân quyền chi
tiết</td></tr><tr><td>Billing</td><td>ErrorLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống Billing
Xóa log loại
ErrorLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Phân quyền chi
tiết</td></tr><tr><td>RPA</td><td>AccessLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống RPA Xóa
log loại AccessLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>AccessLog</td><td>Warning</td><td>Xuất
log</td><td>Hệ thống CRM
Xuất log loại
AccessLog với</td><td>Có thể
truy
xuất khi</td><td>Gửi log sang
ELK</td></tr></tbody></table>

|<image_39>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</th><th>cần</th><th></th></tr></thead><tbody><tr><td>IVR</td><td>PerformanceLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IVR Gửi
log sang SIEM loại
PerformanceLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IPCC</td><td>PerformanceLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống IPCC
Nén và lưu trữ log
loại
PerformanceLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>QA</td><td>TransactionLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống QA Nén
và lưu trữ log loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>QA</td><td>AccessLog</td><td>Error</td><td>Phân
tích
log</td><td>Hệ thống QA Phân
tích log loại
AccessLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>RPA</td><td>AuditLog</td><td>Info</td><td>Phân
tích</td><td>Hệ thống RPA
Phân tích log loại
AuditLog với mức</td><td>Có thể
truy
xuất khi</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_40>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log</th><th>Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</th><th>cần</th><th></th></tr></thead><tbody><tr><td>Billing</td><td>ErrorLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại ErrorLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Có dashboard
Grafana</td></tr><tr><td>CRM</td><td>TransactionLog</td><td>Info</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống CRM
Nén và lưu trữ log
loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>Billing</td><td>TransactionLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống Billing
Xóa log loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>CRM</td><td>TransactionLog</td><td>Error</td><td>Xuất
log</td><td>Hệ thống CRM
Xuất log loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Gửi log sang
ELK</td></tr><tr><td>Infra</td><td>AccessLog</td><td>Warning</td><td>Gửi
log
sang</td><td>Hệ thống Infra Gửi
log sang SIEM loại
AccessLog với</td><td>Có chỉ
số
thống</td><td>Có dashboard
Grafana</td></tr></tbody></table>

|<image_41>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>SIEM</th><th>mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</th><th>kê</th><th></th></tr></thead><tbody><tr><td>IPCC</td><td>AuditLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IPCC
Gửi log sang SIEM
loại AuditLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Gửi log sang
ELK</td></tr><tr><td>CRM</td><td>TransactionLog</td><td>Warning</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống CRM
Nén và lưu trữ log
loại
TransactionLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>IVR</td><td>AccessLog</td><td>Error</td><td>Xuất
log</td><td>Hệ thống IVR Xuất
log loại AccessLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>TransactionLog</td><td>Critical</td><td>Xóa
log</td><td>Hệ thống CRM
Xóa log loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Gửi log sang
ELK</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Fatal</td><td>Nén
và
lưu
trữ</td><td>Hệ thống Infra Nén
và lưu trữ log loại
TransactionLog
với mức Fatal, dữ</td><td>Không
mất mát
dữ liệu</td><td>Theo chuẩn
syslog
RFC5424</td></tr></tbody></table>

|<image_42>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log</th><th>liệu lưu trữ tối
thiểu 90 ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>IPCC</td><td>PerformanceLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống IPCC
Xuất log loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>Billing</td><td>TransactionLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống Billing
Xóa log loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Gửi log sang
ELK</td></tr><tr><td>Infra</td><td>AccessLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại AccessLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IPCC</td><td>TransactionLog</td><td>Info</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IPCC
Gửi log sang SIEM
loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>IPCC</td><td>AccessLog</td><td>Error</td><td>Phân
tích
log</td><td>Hệ thống IPCC
Phân tích log loại
AccessLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr></tbody></table>

|<image_43>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>Infra</td><td>PerformanceLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Infra Gửi
log sang SIEM loại
PerformanceLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>IPCC</td><td>PerformanceLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IPCC
Gửi log sang SIEM
loại
PerformanceLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Billing</td><td>AccessLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại AccessLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Billing</td><td>PerformanceLog</td><td>Info</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Billing
Gửi log sang SIEM
loại
PerformanceLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Có dashboard
Grafana</td></tr><tr><td>CRM</td><td>ErrorLog</td><td>Fatal</td><td>Xuất
log</td><td>Hệ thống CRM
Xuất log loại
ErrorLog với mức
Fatal, dữ liệu lưu</td><td>Có chỉ
số
thống</td><td>Theo chuẩn
syslog
RFC5424</td></tr></tbody></table>

|<image_44>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>trữ tối thiểu 90
ngày.</th><th>kê</th><th></th></tr></thead><tbody><tr><td>Billing</td><td>ErrorLog</td><td>Critical</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại ErrorLog với
mức Critical, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>ErrorLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống CRM
Phân tích log loại
ErrorLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>QA</td><td>AuditLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống QA Gửi
log sang SIEM loại
AuditLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Có dashboard
Grafana</td></tr><tr><td>QA</td><td>PerformanceLog</td><td>Fatal</td><td>Phân
tích
log</td><td>Hệ thống QA Phân
tích log loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống Infra
Xuất log loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr></tbody></table>

|<image_45>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>thiểu 90 ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>CRM</td><td>AuditLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống CRM
Phân tích log loại
AuditLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Phân quyền chi
tiết</td></tr><tr><td>Billing</td><td>AuditLog</td><td>Warning</td><td>Xuất
log</td><td>Hệ thống Billing
Xuất log loại
AuditLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Phân quyền chi
tiết</td></tr><tr><td>IPCC</td><td>AccessLog</td><td>Warning</td><td>Phân
tích
log</td><td>Hệ thống IPCC
Phân tích log loại
AccessLog với
mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>Billing</td><td>PerformanceLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống Billing
Xuất log loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>RPA</td><td>AuditLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống RPA
Xuất log loại
AuditLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Có dashboard
Grafana</td></tr></tbody></table>

|<image_46>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>CRM</td><td>AuditLog</td><td>Critical</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống CRM
Nén và lưu trữ log
loại AuditLog với
mức Critical, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Phân quyền chi
tiết</td></tr><tr><td>RPA</td><td>AuditLog</td><td>Info</td><td>Xuất
log</td><td>Hệ thống RPA
Xuất log loại
AuditLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>RPA</td><td>ErrorLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống RPA
Xuất log loại
ErrorLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>RPA</td><td>ErrorLog</td><td>Error</td><td>Xuất
log</td><td>Hệ thống RPA
Xuất log loại
ErrorLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Phân quyền chi
tiết</td></tr><tr><td>QA</td><td>AuditLog</td><td>Critical</td><td>Xóa
log</td><td>Hệ thống QA Xóa
log loại AuditLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Theo chuẩn
syslog
RFC5424</td></tr></tbody></table>

|<image_47>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>IVR</th><th>AccessLog</th><th>Info</th><th>Gửi
log
sang
SIEM</th><th>Hệ thống IVR Gửi
log sang SIEM loại
AccessLog với
mức Info, dữ liệu
lưu trữ tối thiểu 90
ngày.</th><th>Có thể
truy
xuất khi
cần</th><th>Phân quyền chi
tiết</th></tr></thead><tbody><tr><td>QA</td><td>TransactionLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống QA Gửi
log sang SIEM loại
TransactionLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Infra</td><td>AccessLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống Infra
Phân tích log loại
AccessLog với
mức Critical, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>RPA</td><td>ErrorLog</td><td>Info</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống RPA Gửi
log sang SIEM loại
ErrorLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>CRM</td><td>AccessLog</td><td>Warning</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống CRM
Gửi log sang SIEM
loại AccessLog với
mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr></tbody></table>

|<image_48>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>RPA</th><th>TransactionLog</th><th>Error</th><th>Xóa
log</th><th>Hệ thống RPA Xóa
log loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</th><th>Không
mất mát
dữ liệu</th><th>Phân quyền chi
tiết</th></tr></thead><tbody><tr><td>RPA</td><td>ErrorLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống RPA Gửi
log sang SIEM loại
ErrorLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>RPA</td><td>AuditLog</td><td>Critical</td><td>Xóa
log</td><td>Hệ thống RPA Xóa
log loại AuditLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>ErrorLog</td><td>Warning</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống CRM
Nén và lưu trữ log
loại ErrorLog với
mức Warning, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Có dashboard
Grafana</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>Billing</td><td>PerformanceLog</td><td>Info</td><td>Nén
và</td><td>Hệ thống Billing
Nén và lưu trữ log</td><td>Không
mất mát</td><td>Gửi log sang</td></tr></tbody></table>

|<image_49>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>lưu
trữ
log</th><th>loại
PerformanceLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</th><th>dữ liệu</th><th>ELK</th></tr></thead><tbody><tr><td>Infra</td><td>PerformanceLog</td><td>Fatal</td><td>Phân
tích
log</td><td>Hệ thống Infra
Phân tích log loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Phân quyền chi
tiết</td></tr><tr><td>IPCC</td><td>TransactionLog</td><td>Critical</td><td>Xóa
log</td><td>Hệ thống IPCC
Xóa log loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>IPCC</td><td>PerformanceLog</td><td>Error</td><td>Xóa
log</td><td>Hệ thống IPCC
Xóa log loại
PerformanceLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Gửi log sang
ELK</td></tr><tr><td>Billing</td><td>ErrorLog</td><td>Warning</td><td>Xóa
log</td><td>Hệ thống Billing
Xóa log loại
ErrorLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IVR</td><td>ErrorLog</td><td>Fatal</td><td>Gửi
log</td><td>Hệ thống IVR Gửi
log sang SIEM loại</td><td>Log
được</td><td>Có dashboard</td></tr></tbody></table>

|<image_50>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>sang
SIEM</th><th>ErrorLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</th><th>mã hóa
AES-
256</th><th>Grafana</th></tr></thead><tbody><tr><td>CRM</td><td>PerformanceLog</td><td>Error</td><td>Xuất
log</td><td>Hệ thống CRM
Xuất log loại
PerformanceLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Billing</td><td>TransactionLog</td><td>Critical</td><td>Xóa
log</td><td>Hệ thống Billing
Xóa log loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Phân quyền chi
tiết</td></tr><tr><td>QA</td><td>ErrorLog</td><td>Fatal</td><td>Phân
tích
log</td><td>Hệ thống QA Phân
tích log loại
ErrorLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Có dashboard
Grafana</td></tr><tr><td>Infra</td><td>AuditLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Infra Gửi
log sang SIEM loại
AuditLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>QA</td><td>AuditLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống QA Xuất
log loại AuditLog
với mức Critical,</td><td>Có chỉ
số
thống</td><td>Theo chuẩn
syslog</td></tr></tbody></table>

|<image_51>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th>kê</th><th>RFC5424</th></tr></thead><tbody><tr><td>QA</td><td>PerformanceLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống QA Gửi
log sang SIEM loại
PerformanceLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IVR</td><td>PerformanceLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống IVR Nén
và lưu trữ log loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Có dashboard
Grafana</td></tr><tr><td>CRM</td><td>TransactionLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống CRM
Xóa log loại
TransactionLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Gửi log sang
ELK</td></tr><tr><td>CRM</td><td>AccessLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống CRM
Phân tích log loại
AccessLog với
mức Critical, dữ
liệu lưu trữ tối</td><td>Log
được
mã hóa
AES-</td><td>Theo chuẩn
syslog
RFC5424</td></tr></tbody></table>

|<image_52>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>thiểu 90 ngày.</th><th>256</th><th></th></tr></thead><tbody><tr><td>RPA</td><td>AccessLog</td><td>Error</td><td>Xóa
log</td><td>Hệ thống RPA Xóa
log loại AccessLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Có dashboard
Grafana</td></tr><tr><td>RPA</td><td>AuditLog</td><td>Info</td><td>Xuất
log</td><td>Hệ thống RPA
Xuất log loại
AuditLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>Infra</td><td>ErrorLog</td><td>Warning</td><td>Phân
tích
log</td><td>Hệ thống Infra
Phân tích log loại
ErrorLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>PerformanceLog</td><td>Info</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống CRM
Nén và lưu trữ log
loại
PerformanceLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Có dashboard
Grafana</td></tr><tr><td>Billing</td><td>AuditLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại AuditLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90</td><td>Log
được
mã hóa
AES-
256</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_53>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>IVR</td><td>TransactionLog</td><td>Error</td><td>Phân
tích
log</td><td>Hệ thống IVR
Phân tích log loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>QA</td><td>TransactionLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống QA Nén
và lưu trữ log loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Infra</td><td>AuditLog</td><td>Warning</td><td>Xuất
log</td><td>Hệ thống Infra
Xuất log loại
AuditLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Phân quyền chi
tiết</td></tr><tr><td>IPCC</td><td>PerformanceLog</td><td>Info</td><td>Phân
tích
log</td><td>Hệ thống IPCC
Phân tích log loại
PerformanceLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IVR</td><td>PerformanceLog</td><td>Critical</td><td>Phân
tích
log</td><td>Hệ thống IVR
Phân tích log loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr></tbody></table>

|<image_54>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>thiểu 90 ngày.</th><th></th><th></th></tr></thead><tbody><tr><td>Infra</td><td>ErrorLog</td><td>Critical</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Infra Nén
và lưu trữ log loại
ErrorLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Phân quyền chi
tiết</td></tr><tr><td>QA</td><td>ErrorLog</td><td>Info</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống QA Gửi
log sang SIEM loại
ErrorLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>IVR</td><td>ErrorLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống IVR Xóa
log loại ErrorLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Có dashboard
Grafana</td></tr><tr><td>Billing</td><td>ErrorLog</td><td>Info</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Billing
Gửi log sang SIEM
loại ErrorLog với
mức Info, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Fatal</td><td>Xóa
log</td><td>Hệ thống Infra Xóa
log loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_55>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Billing</th><th>TransactionLog</th><th>Fatal</th><th>Xuất
log</th><th>Hệ thống Billing
Xuất log loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</th><th>Không
mất mát
dữ liệu</th><th>Gửi log sang
ELK</th></tr></thead><tbody><tr><td>IPCC</td><td>ErrorLog</td><td>Warning</td><td>Xóa
log</td><td>Hệ thống IPCC
Xóa log loại
ErrorLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Phân quyền chi
tiết</td></tr><tr><td>IVR</td><td>AccessLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IVR Gửi
log sang SIEM loại
AccessLog với
mức Error, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>Infra</td><td>PerformanceLog</td><td>Fatal</td><td>Phân
tích
log</td><td>Hệ thống Infra
Phân tích log loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Infra</td><td>AuditLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Infra Gửi
log sang SIEM loại
AuditLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_56>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Infra</th><th>AccessLog</th><th>Warning</th><th>Xóa
log</th><th>Hệ thống Infra Xóa
log loại AccessLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th>Có chỉ
số
thống
kê</th><th>Gửi log sang
ELK</th></tr></thead><tbody><tr><td>IVR</td><td>ErrorLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IVR Gửi
log sang SIEM loại
ErrorLog với mức
Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Gửi log sang
ELK</td></tr><tr><td>Infra</td><td>ErrorLog</td><td>Info</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Infra Nén
và lưu trữ log loại
ErrorLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>QA</td><td>TransactionLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống QA Nén
và lưu trữ log loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>RPA</td><td>AccessLog</td><td>Info</td><td>Xóa
log</td><td>Hệ thống RPA Xóa
log loại AccessLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Có dashboard
Grafana</td></tr><tr><td>RPA</td><td>ErrorLog</td><td>Error</td><td>Xuất
log</td><td>Hệ thống RPA
Xuất log loại
ErrorLog với mức</td><td>Có chỉ
số
thống</td><td>Theo chuẩn
syslog</td></tr></tbody></table>

|<image_57>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>Error, dữ liệu lưu
trữ tối thiểu 90
ngày.</th><th>kê</th><th>RFC5424</th></tr></thead><tbody><tr><td>Infra</td><td>ErrorLog</td><td>Critical</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Infra Nén
và lưu trữ log loại
ErrorLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Có dashboard
Grafana</td></tr><tr><td>IPCC</td><td>TransactionLog</td><td>Critical</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IPCC
Gửi log sang SIEM
loại
TransactionLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Infra</td><td>PerformanceLog</td><td>Info</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Infra Gửi
log sang SIEM loại
PerformanceLog
với mức Info, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Phân quyền chi
tiết</td></tr><tr><td>RPA</td><td>PerformanceLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống RPA Nén
và lưu trữ log loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>Billing</td><td>AuditLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống Billing
Xuất log loại
AuditLog với mức</td><td>Có chỉ
số
thống</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_58>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</th><th>kê</th><th></th></tr></thead><tbody><tr><td>IVR</td><td>AuditLog</td><td>Info</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống IVR Gửi
log sang SIEM loại
AuditLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Gửi log sang
ELK</td></tr><tr><td>RPA</td><td>AuditLog</td><td>Warning</td><td>Xuất
log</td><td>Hệ thống RPA
Xuất log loại
AuditLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Có dashboard
Grafana</td></tr><tr><td>IPCC</td><td>AuditLog</td><td>Info</td><td>Phân
tích
log</td><td>Hệ thống IPCC
Phân tích log loại
AuditLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>IVR</td><td>AccessLog</td><td>Fatal</td><td>Xuất
log</td><td>Hệ thống IVR Xuất
log loại AccessLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Không
mất mát
dữ liệu</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>RPA</td><td>ErrorLog</td><td>Warning</td><td>Nén
và
lưu
trữ</td><td>Hệ thống RPA Nén
và lưu trữ log loại
ErrorLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90</td><td>Tích
hợp
cảnh
báo</td><td>Gửi log sang
ELK</td></tr></tbody></table>

|<image_59>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log</th><th>ngày.</th><th>realtime</th><th></th></tr></thead><tbody><tr><td>QA</td><td>AuditLog</td><td>Warning</td><td>Xóa
log</td><td>Hệ thống QA Xóa
log loại AuditLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>IPCC</td><td>ErrorLog</td><td>Info</td><td>Phân
tích
log</td><td>Hệ thống IPCC
Phân tích log loại
ErrorLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Gửi log sang
ELK</td></tr><tr><td>IVR</td><td>ErrorLog</td><td>Warning</td><td>Phân
tích
log</td><td>Hệ thống IVR
Phân tích log loại
ErrorLog với mức
Warning, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Phân quyền chi
tiết</td></tr><tr><td>Infra</td><td>TransactionLog</td><td>Warning</td><td>Xuất
log</td><td>Hệ thống Infra
Xuất log loại
TransactionLog
với mức Warning,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>RPA</td><td>AccessLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống RPA Gửi
log sang SIEM loại
AccessLog với
mức Fatal, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Gửi log sang
ELK</td></tr></tbody></table>

|<image_60>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>CRM</th><th>ErrorLog</th><th>Fatal</th><th>Xóa
log</th><th>Hệ thống CRM
Xóa log loại
ErrorLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</th><th>Log
được
mã hóa
AES-
256</th><th>Tự động xóa
log sau 180
ngày</th></tr></thead><tbody><tr><td>IPCC</td><td>ErrorLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống IPCC
Xuất log loại
ErrorLog với mức
Critical, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Không
mất mát
dữ liệu</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>RPA</td><td>AuditLog</td><td>Info</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống RPA Nén
và lưu trữ log loại
AuditLog với mức
Info, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có thể
truy
xuất khi
cần</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>Billing</td><td>PerformanceLog</td><td>Critical</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống Billing
Nén và lưu trữ log
loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Gửi log sang
ELK</td></tr><tr><td>Infra</td><td>AccessLog</td><td>Critical</td><td>Xuất
log</td><td>Hệ thống Infra
Xuất log loại
AccessLog với
mức Critical, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Phân quyền chi
tiết</td></tr></tbody></table>

|<image_61>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>IVR</th><th>AccessLog</th><th>Critical</th><th>Xuất
log</th><th>Hệ thống IVR Xuất
log loại AccessLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</th><th>Không
mất mát
dữ liệu</th><th>Gửi log sang
ELK</th></tr></thead><tbody><tr><td>Billing</td><td>TransactionLog</td><td>Error</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Billing
Gửi log sang SIEM
loại
TransactionLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Log
được
mã hóa
AES-
256</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>AccessLog</td><td>Info</td><td>Xuất
log</td><td>Hệ thống CRM
Xuất log loại
AccessLog với
mức Info, dữ liệu
lưu trữ tối thiểu 90
ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Tự động xóa
log sau 180
ngày</td></tr><tr><td>CRM</td><td>PerformanceLog</td><td>Critical</td><td>Xóa
log</td><td>Hệ thống CRM
Xóa log loại
PerformanceLog
với mức Critical,
dữ liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Theo chuẩn
syslog
RFC5424</td></tr><tr><td>CRM</td><td>PerformanceLog</td><td>Fatal</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống CRM
Nén và lưu trữ log
loại
PerformanceLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Có chỉ
số
thống
kê</td><td>Tự động xóa
log sau 180
ngày</td></tr></tbody></table>

|<image_62>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD449</th></tr></thead><tbody><tr><td></td><td>BÁO CÁO HỆ THỐNG &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Billing</th><th>TransactionLog</th><th>Fatal</th><th>Nén
và
lưu
trữ
log</th><th>Hệ thống Billing
Nén và lưu trữ log
loại
TransactionLog
với mức Fatal, dữ
liệu lưu trữ tối
thiểu 90 ngày.</th><th>Không
mất mát
dữ liệu</th><th>Tự động xóa
log sau 180
ngày</th></tr></thead><tbody><tr><td>Infra</td><td>AuditLog</td><td>Fatal</td><td>Gửi
log
sang
SIEM</td><td>Hệ thống Infra Gửi
log sang SIEM loại
AuditLog với mức
Fatal, dữ liệu lưu
trữ tối thiểu 90
ngày.</td><td>Có chỉ
số
thống
kê</td><td>Có dashboard
Grafana</td></tr><tr><td>CRM</td><td>PerformanceLog</td><td>Error</td><td>Nén
và
lưu
trữ
log</td><td>Hệ thống CRM
Nén và lưu trữ log
loại
PerformanceLog
với mức Error, dữ
liệu lưu trữ tối
thiểu 90 ngày.</td><td>Tích
hợp
cảnh
báo
realtime</td><td>Theo chuẩn
syslog
RFC5424</td></tr></tbody></table>

|<image_63>|



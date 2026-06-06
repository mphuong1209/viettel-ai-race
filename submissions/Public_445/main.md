# Public_445

<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Nghiệp vụ</th><th>Loại chỉ
tiêu</th><th>Hành
động</th><th>API/Action</th><th>Mô tả chi tiết</th><th></th><th>Phương</th><th></th><th></th><th>Kết quả</th><th></th><th>Ghi chú</th></tr></thead><tbody><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>pháp</td><td></td><td></td><td>mong</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>đo</td><td></td><td></td><td>muốn</td><td></td><td></td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
chức
năng</td><td>Xóa</td><td>/crm/lead/add</td><td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td></td><td></td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td></td><td></td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Gắn
thẻ</td><td>/crm/lead/export</td><td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử
hiệu
năng</td><td></td><td></td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp</td><td></td><td></td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

<table><thead><tr><th>Hành</th></tr></thead><tbody><tr><td>động</td></tr></tbody></table>

|<image_1>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>trước khi
tải.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/lead/export</td><td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Gắn
thẻ</td><td>/crm/lead/export</td><td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/lead/add</td><td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_2>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>AuditLog,
SLA đáp
ứng
99.99%.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/campaign/import</td><td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/lead/add</td><td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử bảo
mật</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_3>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/campaign/import</td><td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Chuyển
đổi</td><td>/crm/campaign/import</td><td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_4>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
chức
năng</th><th>Chuyển
đổi</th><th>/crm/opportunity/delete</th><th>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/campaign/import</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/contact/update</td><td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
hiệu
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_5>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>bộ sang
hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/contact/update</td><td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/contact/update</td><td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_6>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
chức
năng</th><th>Chuyển
đổi</th><th>/crm/contact/update</th><th>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/lead/add</td><td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_7>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>hai lớp
trước khi
tải.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/contact/update</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Xóa</td><td>/crm/lead/export</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_8>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Campaign</th><th>Chỉ tiêu
chức
năng</th><th>Xóa</th><th>/crm/opportunity/delete</th><th>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</th><th>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/lead/add</td><td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Gắn
thẻ</td><td>/crm/lead/add</td><td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_9>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>SLA đáp
ứng
99.99%.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/campaign/import</td><td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/campaign/import</td><td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_10>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
hiệu năng</th><th>Thêm
mới</th><th>/crm/contact/update</th><th>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</th><th>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/opportunity/delete</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/lead/export</td><td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_11>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>ứng
99.99%.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/lead/export</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/lead/export</td><td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_12>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
chức
năng</th><th>Gắn
thẻ</th><th>/crm/contact/update</th><th>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Gắn
thẻ</td><td>/crm/contact/update</td><td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Xóa</td><td>/crm/lead/add</td><td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_13>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/lead/add</td><td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_14>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
bảo mật</th><th>Chuyển
đổi</th><th>/crm/opportunity/delete</th><th>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</th><th>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/lead/add</td><td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/contact/update</td><td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_15>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>rollback
giao dịch.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Chuyển
đổi</td><td>/crm/lead/add</td><td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_16>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Campaign</th><th>Chỉ tiêu
bảo mật</th><th>Xóa</th><th>/crm/campaign/import</th><th>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/campaign/import</td><td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Chuyển
đổi</td><td>/crm/lead/export</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_17>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>vòng 5s,
tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/opportunity/delete</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/campaign/import</td><td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_18>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
bảo mật</th><th>Thêm
mới</th><th>/crm/lead/add</th><th>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</th><th>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
chức
năng</td><td>Cập
nhật</td><td>/crm/lead/add</td><td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_19>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>xác thực
hai lớp
trước khi
tải.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Xóa</td><td>/crm/contact/update</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_20>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Cập
nhật</td><td>/crm/campaign/import</td><td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/opportunity/delete</td><td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_21>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
hiệu năng</th><th>Thêm
mới</th><th>/crm/campaign/import</th><th>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Thêm
mới</td><td>/crm/contact/update</td><td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/opportunity/delete</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_22>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>vòng 5s,
tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Gắn
thẻ</td><td>/crm/campaign/import</td><td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/campaign/import</td><td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_23>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Opportunity</th><th>Chỉ tiêu
hiệu năng</th><th>Gắn
thẻ</th><th>/crm/contact/update</th><th>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</th><th>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Gắn
thẻ</td><td>/crm/campaign/import</td><td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/lead/add</td><td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử bảo
mật</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_24>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>rollback
giao dịch.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/contact/update</td><td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/opportunity/delete</td><td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/opportunity/delete</td><td>Gắn thẻ dữ liệu
Campaign
trong CRM,</td><td>Kiểm
thử</td><td>Cảnh báo
nếu thiếu
trường</td><td>Dữ liệu được
backup hàng ngày,</td></tr></tbody></table>

|<image_25>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>hiệu
năng</th><th>bắt buộc,
hệ thống
rollback
giao dịch.</th><th>lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/opportunity/delete</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Cập
nhật</td><td>/crm/lead/add</td><td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_26>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/opportunity/delete</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/lead/add</td><td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_27>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
chức
năng</th><th>Xóa</th><th>/crm/lead/export</th><th>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/lead/add</td><td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Gắn
thẻ</td><td>/crm/opportunity/delete</td><td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_28>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/contact/update</td><td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Cập
nhật</td><td>/crm/lead/add</td><td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_29>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Opportunity</th><th>Chỉ tiêu
bảo mật</th><th>Export</th><th>/crm/lead/export</th><th>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/lead/add</td><td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Thêm
mới</td><td>/crm/contact/update</td><td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
hiệu
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_30>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>liệu đồng
bộ sang
hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Gắn
thẻ</td><td>/crm/campaign/import</td><td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/lead/export</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_31>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
hiệu năng</th><th>Cập
nhật</th><th>/crm/lead/export</th><th>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/lead/export</td><td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Gắn
thẻ</td><td>/crm/opportunity/delete</td><td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_32>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>SLA đáp
ứng
99.99%.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Gắn
thẻ</td><td>/crm/opportunity/delete</td><td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Export</td><td>/crm/lead/export</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_33>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
chức
năng</th><th>Thêm
mới</th><th>/crm/campaign/import</th><th>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/opportunity/delete</td><td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/lead/add</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_34>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>vòng 5s,
tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/campaign/import</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/contact/update</td><td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_35>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Opportunity</th><th>Chỉ tiêu
chức
năng</th><th>Thêm
mới</th><th>/crm/lead/export</th><th>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/campaign/import</td><td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Xóa</td><td>/crm/opportunity/delete</td><td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu</td><td>Kiểm
thử</td><td>Thành
công với
thời gian
xử lý &lt;</td><td>Dữ liệu được
backup hàng ngày,</td></tr></tbody></table>

|<image_36>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>hiệu
năng</th><th>1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th>lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/lead/export</td><td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/contact/update</td><td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử bảo
mật</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_37>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/contact/update</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/lead/export</td><td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_38>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Opportunity</th><th>Chỉ tiêu
chức
năng</th><th>Thêm
mới</th><th>/crm/contact/update</th><th>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/contact/update</td><td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/opportunity/delete</td><td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu</td><td>Kiểm
thử</td><td>Thành
công với
thời gian
xử lý &lt;</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_39>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>chức
năng</th><th>1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/opportunity/delete</td><td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Chuyển
đổi</td><td>/crm/lead/export</td><td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_40>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Campaign</th><th>Chỉ tiêu
bảo mật</th><th>Export</th><th>/crm/lead/add</th><th>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Cập
nhật</td><td>/crm/lead/export</td><td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Gắn
thẻ</td><td>/crm/opportunity/delete</td><td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_41>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>SLA đáp
ứng
99.99%.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/contact/update</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_42>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Campaign</th><th>Chỉ tiêu
hiệu năng</th><th>Thêm
mới</th><th>/crm/opportunity/delete</th><th>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/campaign/import</td><td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Export</td><td>/crm/lead/export</td><td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_43>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>vòng 5s,
tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
chức
năng</td><td>Gắn
thẻ</td><td>/crm/lead/add</td><td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Gắn
thẻ</td><td>/crm/campaign/import</td><td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_44>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
hiệu năng</th><th>Cập
nhật</th><th>/crm/contact/update</th><th>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/lead/export</td><td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/opportunity/delete</td><td>Export dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_45>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>SLA đáp
ứng
99.99%.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Xóa</td><td>/crm/lead/add</td><td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/lead/export</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_46>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
bảo mật</th><th>Cập
nhật</th><th>/crm/contact/update</th><th>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/lead/add</td><td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Thêm
mới</td><td>/crm/opportunity/delete</td><td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_47>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>hai lớp
trước khi
tải.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/lead/add</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/lead/add</td><td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_48>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
chức
năng</th><th>Export</th><th>/crm/opportunity/delete</th><th>Export dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Chuyển
đổi</td><td>/crm/lead/add</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
hiệu
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_49>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>bộ sang
hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/campaign/import</td><td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Chuyển
đổi</td><td>/crm/lead/add</td><td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_50>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Opportunity</th><th>Chỉ tiêu
chức
năng</th><th>Xóa</th><th>/crm/lead/add</th><th>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/contact/update</td><td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/lead/export</td><td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_51>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>bộ sang
hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/lead/export</td><td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/opportunity/delete</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_52>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
chức
năng</th><th>Thêm
mới</th><th>/crm/campaign/import</th><th>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/campaign/import</td><td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/opportunity/delete</td><td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử bảo
mật</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_53>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>rollback
giao dịch.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/contact/update</td><td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Import</td><td>/crm/campaign/import</td><td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_54>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Campaign</th><th>Chỉ tiêu
hiệu năng</th><th>Xóa</th><th>/crm/campaign/import</th><th>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/lead/export</td><td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/opportunity/delete</td><td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_55>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>SLA đáp
ứng
99.99%.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/lead/add</td><td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/campaign/import</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_56>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
hiệu năng</th><th>Cập
nhật</th><th>/crm/contact/update</th><th>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/lead/add</td><td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Xóa</td><td>/crm/campaign/import</td><td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_57>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>hai lớp
trước khi
tải.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Export</td><td>/crm/lead/add</td><td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Export</td><td>/crm/opportunity/delete</td><td>Export dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_58>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Opportunity</th><th>Chỉ tiêu
chức
năng</th><th>Xóa</th><th>/crm/contact/update</th><th>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/lead/export</td><td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_59>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>rollback
giao dịch.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Thêm
mới</td><td>/crm/campaign/import</td><td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_60>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
hiệu năng</th><th>Thêm
mới</th><th>/crm/lead/add</th><th>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/lead/add</td><td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/lead/export</td><td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_61>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>hai lớp
trước khi
tải.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/lead/add</td><td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_62>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
bảo mật</th><th>Chuyển
đổi</th><th>/crm/lead/add</th><th>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</th><th>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Cập
nhật</td><td>/crm/campaign/import</td><td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Cập
nhật</td><td>/crm/contact/update</td><td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_63>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>ứng
99.99%.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/contact/update</td><td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Gắn
thẻ</td><td>/crm/lead/add</td><td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_64>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
bảo mật</th><th>Xóa</th><th>/crm/lead/export</th><th>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</th><th>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/campaign/import</td><td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/campaign/import</td><td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_65>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>vòng 5s,
tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/campaign/import</td><td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/lead/export</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_66>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th></th><th></th><th>retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Import</td><td>/crm/campaign/import</td><td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/lead/add</td><td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/lead/add</td><td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm</td><td>Kiểm
thử</td><td>Xuất báo
cáo chi
tiết dưới</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_67>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>chức
năng</th><th>dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/opportunity/delete</td><td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Xóa</td><td>/crm/contact/update</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_68>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Chuyển
đổi</td><td>/crm/campaign/import</td><td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Gắn
thẻ</td><td>/crm/contact/update</td><td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Thêm
mới</td><td>/crm/campaign/import</td><td>Thêm mới dữ
liệu Contact</td><td>Kiểm
thử</td><td>Cảnh báo
nếu thiếu</td><td>Dữ liệu được
backup hàng ngày,</td></tr></tbody></table>

|<image_69>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>hiệu
năng</th><th>trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Thêm
mới</td><td>/crm/contact/update</td><td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Export</td><td>/crm/contact/update</td><td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_70>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/opportunity/delete</td><td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/lead/export</td><td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/contact/update</td><td>Import dữ liệu
Lead trong</td><td>Kiểm
thử</td><td>Cảnh báo
nếu thiếu</td><td>Dữ liệu được
backup hàng ngày,</td></tr></tbody></table>

|<image_71>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>hiệu
năng</th><th>trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/lead/export</td><td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Chuyển
đổi</td><td>/crm/lead/export</td><td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_72>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>ứng
99.99%.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/lead/add</td><td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/opportunity/delete</td><td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Export</td><td>/crm/lead/export</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_73>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>hệ thống
rollback
giao dịch.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Xóa</td><td>/crm/contact/update</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/lead/export</td><td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_74>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
chức
năng</th><th>Import</th><th>/crm/campaign/import</th><th>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/lead/export</td><td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/lead/export</td><td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_75>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>rollback
giao dịch.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/campaign/import</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/lead/export</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_76>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
chức
năng</th><th>Thêm
mới</th><th>/crm/contact/update</th><th>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/contact/update</td><td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Xóa</td><td>/crm/lead/export</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_77>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>trong
vòng 5s,
tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Xóa</td><td>/crm/lead/export</td><td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Chuyển
đổi</td><td>/crm/campaign/import</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_78>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Thêm
mới</td><td>/crm/campaign/import</td><td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/campaign/import</td><td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_79>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
chức
năng</th><th>Cập
nhật</th><th>/crm/opportunity/delete</th><th>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Xóa</td><td>/crm/campaign/import</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/lead/export</td><td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử
hiệu
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_80>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>liệu đồng
bộ sang
hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/lead/add</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/lead/add</td><td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_81>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
bảo mật</th><th>Import</th><th>/crm/lead/add</th><th>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Thêm
mới</td><td>/crm/campaign/import</td><td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/lead/add</td><td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_82>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>vòng 5s,
tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/lead/export</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/campaign/import</td><td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_83>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
hiệu năng</th><th>Xóa</th><th>/crm/contact/update</th><th>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/lead/add</td><td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/lead/add</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_84>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>liệu đồng
bộ sang
hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/lead/add</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/campaign/import</td><td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_85>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/opportunity/delete</td><td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Gắn
thẻ</td><td>/crm/campaign/import</td><td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_86>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Campaign</th><th>Chỉ tiêu
hiệu năng</th><th>Cập
nhật</th><th>/crm/campaign/import</th><th>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Import</td><td>/crm/campaign/import</td><td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/lead/export</td><td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_87>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>hai lớp
trước khi
tải.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/lead/add</td><td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Cập
nhật</td><td>/crm/lead/export</td><td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_88>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
chức
năng</th><th>Gắn
thẻ</th><th>/crm/contact/update</th><th>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Thêm
mới</td><td>/crm/lead/export</td><td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/lead/add</td><td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_89>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/opportunity/delete</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Thêm
mới</td><td>/crm/lead/add</td><td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_90>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Campaign</th><th>Chỉ tiêu
bảo mật</th><th>Export</th><th>/crm/contact/update</th><th>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</th><th>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Chuyển
đổi</td><td>/crm/contact/update</td><td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Xóa</td><td>/crm/lead/export</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_91>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>xác thực
hai lớp
trước khi
tải.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/opportunity/delete</td><td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Import</td><td>/crm/campaign/import</td><td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_92>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
bảo mật</th><th>Gắn
thẻ</th><th>/crm/campaign/import</th><th>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</th><th>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/opportunity/delete</td><td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/opportunity/delete</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_93>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>hai lớp
trước khi
tải.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/opportunity/delete</td><td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Thêm
mới</td><td>/crm/lead/export</td><td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_94>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
chức
năng</th><th>Cập
nhật</th><th>/crm/lead/add</th><th>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/campaign/import</td><td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Import</td><td>/crm/lead/export</td><td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử bảo
mật</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_95>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>rollback
giao dịch.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/contact/update</td><td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/lead/add</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/campaign/import</td><td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_96>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Export</td><td>/crm/opportunity/delete</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/opportunity/delete</td><td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_97>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/opportunity/delete</td><td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/lead/export</td><td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_98>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Opportunity</th><th>Chỉ tiêu
bảo mật</th><th>Thêm
mới</th><th>/crm/contact/update</th><th>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</th><th>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Chuyển
đổi</td><td>/crm/opportunity/delete</td><td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/lead/export</td><td>Cập nhật dữ
liệu Campaign
trong CRM,</td><td>Kiểm
thử</td><td>Đồng bộ
dữ liệu
sang</td><td>Yêu cầu tích hợp
với hệ thống RPA</td></tr></tbody></table>

|<image_99>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>hiệu
năng</th><th>DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>để tự động hóa quy
trình.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Gắn
thẻ</td><td>/crm/lead/add</td><td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/contact/update</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_100>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>ứng
99.99%.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Gắn
thẻ</td><td>/crm/contact/update</td><td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/opportunity/delete</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_101>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>hệ thống
rollback
giao dịch.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Xóa</td><td>/crm/lead/export</td><td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Thêm
mới</td><td>/crm/lead/export</td><td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_102>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
hiệu năng</th><th>Thêm
mới</th><th>/crm/contact/update</th><th>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/lead/add</td><td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Import</td><td>/crm/contact/update</td><td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_103>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>hai lớp
trước khi
tải.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Import</td><td>/crm/contact/update</td><td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/lead/add</td><td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_104>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
chức
năng</th><th>Gắn
thẻ</th><th>/crm/lead/export</th><th>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/contact/update</td><td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Xóa</td><td>/crm/opportunity/delete</td><td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_105>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>rollback
giao dịch.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/campaign/import</td><td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/opportunity/delete</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_106>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
hiệu năng</th><th>Xóa</th><th>/crm/opportunity/delete</th><th>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Import</td><td>/crm/lead/export</td><td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
chức
năng</td><td>Import</td><td>/crm/contact/update</td><td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_107>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>rollback
giao dịch.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/opportunity/delete</td><td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/lead/add</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_108>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
hiệu năng</th><th>Xóa</th><th>/crm/contact/update</th><th>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</th><th>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/opportunity/delete</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/lead/add</td><td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_109>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>rollback
giao dịch.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Xóa</td><td>/crm/lead/add</td><td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_110>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Campaign</th><th>Chỉ tiêu
bảo mật</th><th>Thêm
mới</th><th>/crm/lead/add</th><th>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
hiệu
năng</th><th>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Thêm
mới</td><td>/crm/campaign/import</td><td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/campaign/import</td><td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_111>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/lead/export</td><td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
chức
năng</td><td>Xóa</td><td>/crm/lead/add</td><td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_112>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Opportunity</th><th>Chỉ tiêu
hiệu năng</th><th>Chuyển
đổi</th><th>/crm/lead/add</th><th>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/lead/add</td><td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/lead/export</td><td>Export dữ liệu
Opportunity
trong CRM,
bao gồm</td><td>Kiểm
thử</td><td>Không
lỗi, log
đầy đủ
trong</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_113>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>hiệu
năng</th><th>AuditLog,
SLA đáp
ứng
99.99%.</th><th></th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Cập
nhật</td><td>/crm/contact/update</td><td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/opportunity/delete</td><td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_114>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th></th><th></th><th>retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Xóa</td><td>/crm/campaign/import</td><td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Thêm
mới</td><td>/crm/lead/export</td><td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_115>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Lead</th><th>Chỉ tiêu
hiệu năng</th><th>Xóa</th><th>/crm/contact/update</th><th>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Chuyển
đổi</td><td>/crm/opportunity/delete</td><td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Cập
nhật</td><td>/crm/lead/add</td><td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm</td><td>Kiểm
thử</td><td>Đồng bộ
dữ liệu
sang
DataLake</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr></tbody></table>

|<image_116>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>hiệu
năng</th><th>trong
vòng 5s,
tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/lead/add</td><td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/lead/export</td><td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_117>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Cập
nhật</td><td>/crm/lead/add</td><td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/lead/export</td><td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
bảo mật</td><td>Xóa</td><td>/crm/contact/update</td><td>Xóa dữ liệu
Contact trong</td><td>Kiểm
thử</td><td>Cảnh báo
nếu thiếu</td><td>Kết quả được gửi
mail và SMS cho</td></tr></tbody></table>

|<image_118>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>hiệu
năng</th><th>trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Import</td><td>/crm/opportunity/delete</td><td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
bảo mật</td><td>Gắn
thẻ</td><td>/crm/lead/add</td><td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td><td>Kiểm
thử bảo
mật</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_119>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>và ghi log đầy
đủ.</th><th></th><th>hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/lead/export</td><td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Thêm
mới</td><td>/crm/campaign/import</td><td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_120>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Opportunity</th><th>Chỉ tiêu
bảo mật</th><th>Chuyển
đổi</th><th>/crm/opportunity/delete</th><th>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Export</td><td>/crm/opportunity/delete</td><td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Xóa</td><td>/crm/campaign/import</td><td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm</td><td>Kiểm
thử bảo
mật</td><td>Đồng bộ
dữ liệu
sang
DataLake</td><td>Kết quả được gửi
mail và SMS cho</td></tr></tbody></table>

|<image_121>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Xóa</td><td>/crm/lead/add</td><td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Export</td><td>/crm/contact/update</td><td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr></tbody></table>

|<image_122>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Campaign</th><th>Chỉ tiêu
chức
năng</th><th>Chuyển
đổi</th><th>/crm/contact/update</th><th>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Chuyển
đổi</td><td>/crm/lead/export</td><td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Thêm
mới</td><td>/crm/lead/add</td><td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm</td><td>Kiểm
thử</td><td>Đồng bộ
dữ liệu
sang
DataLake</td><td>Kết quả được gửi
mail và SMS cho</td></tr></tbody></table>

|<image_123>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>chức
năng</th><th>trong
vòng 5s,
tự động
retry khi
lỗi.</th><th>quản trị viên phụ
trách.</th></tr></thead><tbody><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Export</td><td>/crm/contact/update</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
hiệu năng</td><td>Gắn
thẻ</td><td>/crm/contact/update</td><td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_124>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
chức
năng</th><th>Xóa</th><th>/crm/lead/add</th><th>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</th><th>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</th></tr></thead><tbody><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Import</td><td>/crm/campaign/import</td><td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr><tr><td>Contact</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/lead/export</td><td>Export dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td><td>Kiểm
thử
hiệu
năng</td><td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_125>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>xác thực
hai lớp
trước khi
tải.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Gắn
thẻ</td><td>/crm/contact/update</td><td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
chức
năng</td><td>Import</td><td>/crm/lead/export</td><td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử bảo
mật</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_126>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
hiệu năng</th><th>Xóa</th><th>/crm/opportunity/delete</th><th>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử
chức
năng</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/lead/export</td><td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Thêm
mới</td><td>/crm/opportunity/delete</td><td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu</td><td>Kiểm
thử
hiệu
năng</td><td>Đồng bộ
dữ liệu
sang
DataLake
trong</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_127>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th></th><th>vòng 5s,
tự động
retry khi
lỗi.</th><th></th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
bảo mật</td><td>Thêm
mới</td><td>/crm/lead/export</td><td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td><td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td></tr><tr><td>Lead</td><td>Chỉ tiêu
hiệu năng</td><td>Export</td><td>/crm/opportunity/delete</td><td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Thành
công với
thời gian
xử lý &lt;
1s, dữ
liệu đồng
bộ sang</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr></tbody></table>

|<image_128>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th></th><th></th><th></th><th>hệ thống
Billing.</th><th></th></tr></thead><tbody><tr><td>Campaign</td><td>Chỉ tiêu
bảo mật</td><td>Xóa</td><td>/crm/lead/add</td><td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td></tr><tr><td>Campaign</td><td>Chỉ tiêu
chức
năng</td><td>Chuyển
đổi</td><td>/crm/opportunity/delete</td><td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
chức
năng</td><td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td><td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td></tr></tbody></table>

|<image_129>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD445</th></tr></thead><tbody><tr><td></td><td>CHỈ TIÊU CRM - RPA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Contact</th><th>Chỉ tiêu
hiệu năng</th><th>Export</th><th>/crm/lead/add</th><th>Export dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</th><th>Kiểm
thử bảo
mật</th><th>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</th><th>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</th></tr></thead><tbody><tr><td>Opportunity</td><td>Chỉ tiêu
hiệu năng</td><td>Thêm
mới</td><td>/crm/lead/export</td><td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td><td>Kiểm
thử
hiệu
năng</td><td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td><td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td></tr></tbody></table>

|<image_130>|



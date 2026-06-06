# Public_448

<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>API</th><th></th><th>Phương</th><th></th><th></th><th>Hành</th><th></th><th>Mô tả chi tiết</th><th>Kết quả</th><th>Ghi chú</th></tr></thead><tbody><tr><td></td><td></td><td>thức</td><td></td><td></td><td>động</td><td></td><td></td><td></td><td></td></tr><tr><td>/customer/update</td><td>PATCH</td><td></td><td></td><td>Thêm
bản
ghi</td><td></td><td></td><td>API /customer/update
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>PATCH</td><td></td><td></td><td>Xóa
thông
tin</td><td></td><td></td><td>API /invoice/export sử
dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/security/firewall/config</td><td>GET</td><td></td><td></td><td>Xóa
thông
tin</td><td></td><td></td><td>API
/security/firewall/config
sử dụng phương thức
GET để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/ivr/callflow</td><td>POST</td><td></td><td></td><td>Kiểm
tra
trạng
thái</td><td></td><td></td><td>API /ivr/callflow sử
dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Có
versioning
v1/v2</td></tr><tr><td>/crm/lead/import</td><td>PUT</td><td></td><td></td><td>Export
dữ
liệu</td><td></td><td></td><td>API /crm/lead/import
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Tích hợp
với API
Gateway</td></tr></tbody></table>

|<image_1>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/rpa/task/execute</th><th>POST</th><th>Cập
nhật
cấu
hình</th><th>API /rpa/task/execute
sử dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>Log đầy
đủ</th><th>Tích hợp
với API
Gateway</th></tr></thead><tbody><tr><td>/customer/update</td><td>GET</td><td>Thêm
bản
ghi</td><td>API /customer/update
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/network/qos/monitor</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API
/network/qos/monitor
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/invoice/export</td><td>POST</td><td>Cập
nhật
cấu
hình</td><td>API /invoice/export sử
dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/network/qos/monitor</td><td>GET</td><td>Export
dữ
liệu</td><td>API
/network/qos/monitor
sử dụng phương thức
GET để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr></tbody></table>

|<image_2>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/rpa/task/execute</th><th>POST</th><th>Export
dữ
liệu</th><th>API /rpa/task/execute
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>Log đầy
đủ</th><th>Giới hạn
rate-limit
1000
req/min</th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>PATCH</td><td>Export
dữ
liệu</td><td>API /crm/lead/import
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>POST</td><td>Cập
nhật
cấu
hình</td><td>API /invoice/export sử
dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/ivr/callflow</td><td>GET</td><td>Xóa
thông
tin</td><td>API /ivr/callflow sử
dụng phương thức GET
để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/security/firewall/config</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Tích hợp
với API
Gateway</td></tr></tbody></table>

|<image_3>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/ivr/callflow</th><th>POST</th><th>Xóa
thông
tin</th><th>API /ivr/callflow sử
dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</th><th>Thành
công
&lt;1s</th><th>Theo
chuẩn
RESTful</th></tr></thead><tbody><tr><td>/security/firewall/config</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>GET</td><td>Thêm
bản
ghi</td><td>API /invoice/export sử
dụng phương thức GET
để Thêm bản ghi, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/invoice/export</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /invoice/export sử
dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>PUT</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/ivr/callflow</td><td>PUT</td><td>Thêm
bản</td><td>API /ivr/callflow sử
dụng phương thức PUT</td><td>Log đầy</td><td>Tích hợp
với API</td></tr></tbody></table>

|<image_4>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>ghi</th><th>để Thêm bản ghi, có
xác thực OAuth2 và log
giao dịch chi tiết.</th><th>đủ</th><th>Gateway</th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>POST</td><td>Thêm
bản
ghi</td><td>API /rpa/task/execute
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/rpa/task/execute</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /rpa/task/execute
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /crm/lead/import
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Có
versioning
v1/v2</td></tr><tr><td>/crm/lead/import</td><td>DELETE</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/network/qos/monitor</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Thêm bản</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr></tbody></table>

|<image_5>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API /crm/lead/import
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/rpa/task/execute</td><td>PATCH</td><td>Cập
nhật
cấu
hình</td><td>API /rpa/task/execute
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/invoice/export</td><td>GET</td><td>Export
dữ
liệu</td><td>API /invoice/export sử
dụng phương thức GET
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/security/firewall/config</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/rpa/task/execute</td><td>POST</td><td>Kiểm
tra
trạng</td><td>API /rpa/task/execute
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr></tbody></table>

|<image_6>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>thái</th><th>OAuth2 và log giao
dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/security/firewall/config</td><td>GET</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/rpa/task/execute</td><td>GET</td><td>Thêm
bản
ghi</td><td>API /rpa/task/execute
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/crm/lead/import</td><td>POST</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/ivr/callflow</td><td>GET</td><td>Export
dữ
liệu</td><td>API /ivr/callflow sử
dụng phương thức GET
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/ivr/callflow</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API /ivr/callflow sử
dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr></tbody></table>

|<image_7>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/invoice/export</td><td>PUT</td><td>Export
dữ
liệu</td><td>API /invoice/export sử
dụng phương thức PUT
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/ivr/callflow</td><td>PATCH</td><td>Export
dữ
liệu</td><td>API /ivr/callflow sử
dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/invoice/export</td><td>PUT</td><td>Export
dữ
liệu</td><td>API /invoice/export sử
dụng phương thức PUT
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/customer/update</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /customer/update
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Có
versioning
v1/v2</td></tr><tr><td>/rpa/task/execute</td><td>DELETE</td><td>Cập
nhật
cấu
hình</td><td>API /rpa/task/execute
sử dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/security/firewall/config</td><td>PUT</td><td>Export</td><td>API</td><td>Rollback</td><td>Tích hợp</td></tr></tbody></table>

|<image_8>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>dữ
liệu</th><th>/security/firewall/config
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</th><th>khi lỗi</th><th>với API
Gateway</th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>PUT</td><td>Export
dữ
liệu</td><td>API /rpa/task/execute
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/security/firewall/config</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API
/security/firewall/config
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/network/qos/monitor</td><td>DELETE</td><td>Export
dữ
liệu</td><td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/rpa/task/execute</td><td>PATCH</td><td>Thêm
bản
ghi</td><td>API /rpa/task/execute
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>GET</td><td>Xóa
thông</td><td>API /invoice/export sử
dụng phương thức GET</td><td>Rollback</td><td>Giới hạn
rate-limit</td></tr></tbody></table>

|<image_9>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>tin</th><th>để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</th><th>khi lỗi</th><th>1000
req/min</th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>PATCH</td><td>Cập
nhật
cấu
hình</td><td>API /rpa/task/execute
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/ivr/callflow</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /ivr/callflow sử
dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API /invoice/export sử
dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/rpa/task/execute</td><td>GET</td><td>Cập
nhật
cấu
hình</td><td>API /rpa/task/execute
sử dụng phương thức
GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/ivr/callflow</td><td>DELETE</td><td>Cập
nhật
cấu</td><td>API /ivr/callflow sử
dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr></tbody></table>

|<image_10>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>hình</th><th>OAuth2 và log giao
dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>PUT</td><td>Xóa
thông
tin</td><td>API /crm/lead/import
sử dụng phương thức
PUT để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Có
versioning
v1/v2</td></tr><tr><td>/crm/lead/import</td><td>POST</td><td>Thêm
bản
ghi</td><td>API /crm/lead/import
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/network/qos/monitor</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/customer/update</td><td>PATCH</td><td>Xóa
thông
tin</td><td>API /customer/update
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>POST</td><td>Export
dữ
liệu</td><td>API /crm/lead/import
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao</td><td>Log đầy
đủ</td><td>Giới hạn
rate-limit
1000
req/min</td></tr></tbody></table>

|<image_11>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/security/firewall/config</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API
/security/firewall/config
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/invoice/export</td><td>GET</td><td>Export
dữ
liệu</td><td>API /invoice/export sử
dụng phương thức GET
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/security/firewall/config</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/customer/update</td><td>GET</td><td>Cập
nhật
cấu
hình</td><td>API /customer/update
sử dụng phương thức
GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/customer/update</td><td>POST</td><td>Xóa
thông
tin</td><td>API /customer/update
sử dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr></tbody></table>

|<image_12>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/network/qos/monitor</th><th>PUT</th><th>Thêm
bản
ghi</th><th>API
/network/qos/monitor
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</th><th>Retry tối
đa 3 lần</th><th>Có
versioning
v1/v2</th></tr></thead><tbody><tr><td>/ivr/callflow</td><td>DELETE</td><td>Export
dữ
liệu</td><td>API /ivr/callflow sử
dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>GET</td><td>Xóa
thông
tin</td><td>API /invoice/export sử
dụng phương thức GET
để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Có
versioning
v1/v2</td></tr><tr><td>/security/firewall/config</td><td>GET</td><td>Export
dữ
liệu</td><td>API
/security/firewall/config
sử dụng phương thức
GET để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/ivr/callflow</td><td>POST</td><td>Xóa
thông
tin</td><td>API /ivr/callflow sử
dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/customer/update</td><td>DELETE</td><td>Xóa
thông</td><td>API /customer/update
sử dụng phương thức
DELETE để Xóa thông</td><td>Rollback
khi lỗi</td><td>Giới hạn
rate-limit
1000</td></tr></tbody></table>

|<image_13>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>tin</th><th>tin, có xác thực OAuth2
và log giao dịch chi tiết.</th><th></th><th>req/min</th></tr></thead><tbody><tr><td>/security/firewall/config</td><td>POST</td><td>Thêm
bản
ghi</td><td>API
/security/firewall/config
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/invoice/export</td><td>GET</td><td>Thêm
bản
ghi</td><td>API /invoice/export sử
dụng phương thức GET
để Thêm bản ghi, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/customer/update</td><td>PUT</td><td>Kiểm
tra
trạng
thái</td><td>API /customer/update
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/customer/update</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API /customer/update
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/ivr/callflow</td><td>POST</td><td>Export
dữ
liệu</td><td>API /ivr/callflow sử
dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao</td><td>Thành
công
&lt;1s</td><td>Có
versioning
v1/v2</td></tr></tbody></table>

|<image_14>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/invoice/export</td><td>DELETE</td><td>Export
dữ
liệu</td><td>API /invoice/export sử
dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Có
versioning
v1/v2</td></tr><tr><td>/security/firewall/config</td><td>GET</td><td>Export
dữ
liệu</td><td>API
/security/firewall/config
sử dụng phương thức
GET để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>PATCH</td><td>Xóa
thông
tin</td><td>API /crm/lead/import
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/network/qos/monitor</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API
/network/qos/monitor
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/crm/lead/import</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API /crm/lead/import
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao</td><td>Log đầy
đủ</td><td>Giới hạn
rate-limit
1000
req/min</td></tr></tbody></table>

|<image_15>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>PUT</td><td>Export
dữ
liệu</td><td>API /crm/lead/import
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Có
versioning
v1/v2</td></tr><tr><td>/crm/lead/import</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API /crm/lead/import
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/customer/update</td><td>GET</td><td>Kiểm
tra
trạng
thái</td><td>API /customer/update
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/network/qos/monitor</td><td>PUT</td><td>Cập
nhật
cấu
hình</td><td>API
/network/qos/monitor
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/network/qos/monitor</td><td>PUT</td><td>Kiểm
tra
trạng
thái</td><td>API
/network/qos/monitor
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr></tbody></table>

|<image_16>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/security/firewall/config</td><td>GET</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/security/firewall/config</td><td>GET</td><td>Cập
nhật
cấu
hình</td><td>API
/security/firewall/config
sử dụng phương thức
GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>POST</td><td>Thêm
bản
ghi</td><td>API /invoice/export sử
dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/security/firewall/config</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/network/qos/monitor</td><td>GET</td><td>Cập
nhật
cấu</td><td>API
/network/qos/monitor
sử dụng phương thức</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API</td></tr></tbody></table>

|<image_17>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>hình</th><th>GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th></th><th>Gateway</th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>PATCH</td><td>Export
dữ
liệu</td><td>API /rpa/task/execute
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/customer/update</td><td>PUT</td><td>Xóa
thông
tin</td><td>API /customer/update
sử dụng phương thức
PUT để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/customer/update</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API /customer/update
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Có
versioning
v1/v2</td></tr><tr><td>/ivr/callflow</td><td>GET</td><td>Kiểm
tra
trạng
thái</td><td>API /ivr/callflow sử
dụng phương thức GET
để Kiểm tra trạng thái,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>PUT</td><td>Export
dữ
liệu</td><td>API /invoice/export sử
dụng phương thức PUT
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr></tbody></table>

|<image_18>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/security/firewall/config</th><th>DELETE</th><th>Xóa
thông
tin</th><th>API
/security/firewall/config
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</th><th>Rollback
khi lỗi</th><th>Tích hợp
với API
Gateway</th></tr></thead><tbody><tr><td>/network/qos/monitor</td><td>DELETE</td><td>Export
dữ
liệu</td><td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/crm/lead/import</td><td>PATCH</td><td>Xóa
thông
tin</td><td>API /crm/lead/import
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/invoice/export</td><td>POST</td><td>Thêm
bản
ghi</td><td>API /invoice/export sử
dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/rpa/task/execute</td><td>POST</td><td>Cập
nhật
cấu
hình</td><td>API /rpa/task/execute
sử dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API
Gateway</td></tr></tbody></table>

|<image_19>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/crm/lead/import</th><th>GET</th><th>Kiểm
tra
trạng
thái</th><th>API /crm/lead/import
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>Retry tối
đa 3 lần</th><th>Theo
chuẩn
RESTful</th></tr></thead><tbody><tr><td>/network/qos/monitor</td><td>PUT</td><td>Kiểm
tra
trạng
thái</td><td>API
/network/qos/monitor
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/customer/update</td><td>POST</td><td>Cập
nhật
cấu
hình</td><td>API /customer/update
sử dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API /crm/lead/import
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/ivr/callflow</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API /ivr/callflow sử
dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Giới hạn
rate-limit
1000
req/min</td></tr></tbody></table>

|<image_20>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/customer/update</th><th>PATCH</th><th>Cập
nhật
cấu
hình</th><th>API /customer/update
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>Log đầy
đủ</th><th>Tích hợp
với API
Gateway</th></tr></thead><tbody><tr><td>/invoice/export</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API /invoice/export sử
dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>PATCH</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Có
versioning
v1/v2</td></tr><tr><td>/customer/update</td><td>GET</td><td>Kiểm
tra
trạng
thái</td><td>API /customer/update
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/crm/lead/import</td><td>PATCH</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Tích hợp
với API
Gateway</td></tr></tbody></table>

|<image_21>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/crm/lead/import</th><th>GET</th><th>Thêm
bản
ghi</th><th>API /crm/lead/import
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</th><th>Thành
công
&lt;1s</th><th>Tích hợp
với API
Gateway</th></tr></thead><tbody><tr><td>/security/firewall/config</td><td>GET</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Có
versioning
v1/v2</td></tr><tr><td>/crm/lead/import</td><td>PATCH</td><td>Export
dữ
liệu</td><td>API /crm/lead/import
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/network/qos/monitor</td><td>GET</td><td>Kiểm
tra
trạng
thái</td><td>API
/network/qos/monitor
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/security/firewall/config</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao</td><td>Retry tối
đa 3 lần</td><td>Hỗ trợ
JSON và
XML</td></tr></tbody></table>

|<image_22>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/customer/update</td><td>POST</td><td>Export
dữ
liệu</td><td>API /customer/update
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/ivr/callflow</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /ivr/callflow sử
dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr><tr><td>/network/qos/monitor</td><td>GET</td><td>Cập
nhật
cấu
hình</td><td>API
/network/qos/monitor
sử dụng phương thức
GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/network/qos/monitor</td><td>PUT</td><td>Export
dữ
liệu</td><td>API
/network/qos/monitor
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/ivr/callflow</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /ivr/callflow sử
dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao</td><td>Rollback
khi lỗi</td><td>Theo
chuẩn
RESTful</td></tr></tbody></table>

|<image_23>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>PUT</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>POST</td><td>Xóa
thông
tin</td><td>API /crm/lead/import
sử dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/network/qos/monitor</td><td>PATCH</td><td>Export
dữ
liệu</td><td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/ivr/callflow</td><td>PUT</td><td>Cập
nhật
cấu
hình</td><td>API /ivr/callflow sử
dụng phương thức PUT
để Cập nhật cấu hình,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/ivr/callflow</td><td>GET</td><td>Cập
nhật
cấu
hình</td><td>API /ivr/callflow sử
dụng phương thức GET
để Cập nhật cấu hình,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>PATCH</td><td>Thêm</td><td>API /crm/lead/import</td><td>Thông</td><td>Theo</td></tr></tbody></table>

|<image_24>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>bản
ghi</th><th>sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>báo sự
kiện qua
Kafka</th><th>chuẩn
RESTful</th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>PATCH</td><td>Thêm
bản
ghi</td><td>API /rpa/task/execute
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/ivr/callflow</td><td>PATCH</td><td>Export
dữ
liệu</td><td>API /ivr/callflow sử
dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>PUT</td><td>Cập
nhật
cấu
hình</td><td>API /invoice/export sử
dụng phương thức PUT
để Cập nhật cấu hình,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/network/qos/monitor</td><td>DELETE</td><td>Export
dữ
liệu</td><td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/crm/lead/import</td><td>PUT</td><td>Cập
nhật</td><td>API /crm/lead/import
sử dụng phương thức</td><td>Rollback</td><td>Theo
chuẩn</td></tr></tbody></table>

|<image_25>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>cấu
hình</th><th>PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>khi lỗi</th><th>RESTful</th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>POST</td><td>Cập
nhật
cấu
hình</td><td>API /rpa/task/execute
sử dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/rpa/task/execute</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /rpa/task/execute
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/network/qos/monitor</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API
/network/qos/monitor
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr><tr><td>/customer/update</td><td>GET</td><td>Xóa
thông
tin</td><td>API /customer/update
sử dụng phương thức
GET để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/rpa/task/execute</td><td>POST</td><td>Kiểm
tra
trạng</td><td>API /rpa/task/execute
sử dụng phương thức
POST để Kiểm tra</td><td>Thành
công</td><td>Giới hạn
rate-limit
1000</td></tr></tbody></table>

|<image_26>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>thái</th><th>trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>&lt;1s</th><th>req/min</th></tr></thead><tbody><tr><td>/security/firewall/config</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API
/security/firewall/config
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Có
versioning
v1/v2</td></tr><tr><td>/security/firewall/config</td><td>DELETE</td><td>Xóa
thông
tin</td><td>API
/security/firewall/config
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/customer/update</td><td>PATCH</td><td>Xóa
thông
tin</td><td>API /customer/update
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/security/firewall/config</td><td>PATCH</td><td>Cập
nhật
cấu
hình</td><td>API
/security/firewall/config
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Có
versioning
v1/v2</td></tr><tr><td>/network/qos/monitor</td><td>GET</td><td>Cập
nhật
cấu</td><td>API
/network/qos/monitor
sử dụng phương thức</td><td>Rollback
khi lỗi</td><td>Tích hợp
với API</td></tr></tbody></table>

|<image_27>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>hình</th><th>GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th></th><th>Gateway</th></tr></thead><tbody><tr><td>/customer/update</td><td>PUT</td><td>Kiểm
tra
trạng
thái</td><td>API /customer/update
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/ivr/callflow</td><td>POST</td><td>Cập
nhật
cấu
hình</td><td>API /ivr/callflow sử
dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/security/firewall/config</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/invoice/export</td><td>POST</td><td>Export
dữ
liệu</td><td>API /invoice/export sử
dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/security/firewall/config</td><td>POST</td><td>Xóa
thông</td><td>API
/security/firewall/config</td><td>Retry tối</td><td>Hỗ trợ
JSON và</td></tr></tbody></table>

|<image_28>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>tin</th><th>sử dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</th><th>đa 3 lần</th><th>XML</th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>POST</td><td>Thêm
bản
ghi</td><td>API /crm/lead/import
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/network/qos/monitor</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/ivr/callflow</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /ivr/callflow sử
dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Có
versioning
v1/v2</td></tr><tr><td>/network/qos/monitor</td><td>PATCH</td><td>Export
dữ
liệu</td><td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API
Gateway</td></tr></tbody></table>

|<image_29>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/rpa/task/execute</th><th>PATCH</th><th>Cập
nhật
cấu
hình</th><th>API /rpa/task/execute
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>Retry tối
đa 3 lần</th><th>Tích hợp
với API
Gateway</th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>GET</td><td>Thêm
bản
ghi</td><td>API /crm/lead/import
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/invoice/export</td><td>DELETE</td><td>Xóa
thông
tin</td><td>API /invoice/export sử
dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/customer/update</td><td>GET</td><td>Kiểm
tra
trạng
thái</td><td>API /customer/update
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr><tr><td>/rpa/task/execute</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API /rpa/task/execute
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/crm/lead/import</td><td>POST</td><td>Xóa
thông</td><td>API /crm/lead/import
sử dụng phương thức
POST để Xóa thông tin,</td><td>Thành
công</td><td>Tích hợp
với API</td></tr></tbody></table>

|<image_30>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>tin</th><th>có xác thực OAuth2 và
log giao dịch chi tiết.</th><th>&lt;1s</th><th>Gateway</th></tr></thead><tbody><tr><td>/network/qos/monitor</td><td>PATCH</td><td>Thêm
bản
ghi</td><td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/ivr/callflow</td><td>GET</td><td>Xóa
thông
tin</td><td>API /ivr/callflow sử
dụng phương thức GET
để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/customer/update</td><td>PATCH</td><td>Export
dữ
liệu</td><td>API /customer/update
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/invoice/export</td><td>POST</td><td>Export
dữ
liệu</td><td>API /invoice/export sử
dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Có
versioning
v1/v2</td></tr><tr><td>/invoice/export</td><td>PUT</td><td>Xóa
thông
tin</td><td>API /invoice/export sử
dụng phương thức PUT
để Xóa thông tin, có
xác thực OAuth2 và log</td><td>Log đầy
đủ</td><td>Hỗ trợ
JSON và
XML</td></tr></tbody></table>

|<image_31>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>giao dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/network/qos/monitor</td><td>PATCH</td><td>Thêm
bản
ghi</td><td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr><tr><td>/rpa/task/execute</td><td>GET</td><td>Kiểm
tra
trạng
thái</td><td>API /rpa/task/execute
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/customer/update</td><td>PATCH</td><td>Xóa
thông
tin</td><td>API /customer/update
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /invoice/export sử
dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/rpa/task/execute</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API /rpa/task/execute
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Có
versioning
v1/v2</td></tr></tbody></table>

|<image_32>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/invoice/export</th><th>PATCH</th><th>Xóa
thông
tin</th><th>API /invoice/export sử
dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</th><th>Thành
công
&lt;1s</th><th>Tích hợp
với API
Gateway</th></tr></thead><tbody><tr><td>/ivr/callflow</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API /ivr/callflow sử
dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>GET</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/rpa/task/execute</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /rpa/task/execute
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/network/qos/monitor</td><td>PATCH</td><td>Cập
nhật
cấu
hình</td><td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API
Gateway</td></tr></tbody></table>

|<image_33>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/ivr/callflow</th><th>POST</th><th>Export
dữ
liệu</th><th>API /ivr/callflow sử
dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>Rollback
khi lỗi</th><th>Hỗ trợ
JSON và
XML</th></tr></thead><tbody><tr><td>/ivr/callflow</td><td>DELETE</td><td>Cập
nhật
cấu
hình</td><td>API /ivr/callflow sử
dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>GET</td><td>Xóa
thông
tin</td><td>API /crm/lead/import
sử dụng phương thức
GET để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/rpa/task/execute</td><td>PUT</td><td>Xóa
thông
tin</td><td>API /rpa/task/execute
sử dụng phương thức
PUT để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/crm/lead/import</td><td>PATCH</td><td>Thêm
bản
ghi</td><td>API /crm/lead/import
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr><tr><td>/invoice/export</td><td>PUT</td><td>Kiểm
tra
trạng</td><td>API /invoice/export sử
dụng phương thức PUT
để Kiểm tra trạng thái,</td><td>Retry tối
đa 3 lần</td><td>Theo
chuẩn</td></tr></tbody></table>

|<image_34>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>thái</th><th>có xác thực OAuth2 và
log giao dịch chi tiết.</th><th></th><th>RESTful</th></tr></thead><tbody><tr><td>/ivr/callflow</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /ivr/callflow sử
dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/invoice/export</td><td>GET</td><td>Kiểm
tra
trạng
thái</td><td>API /invoice/export sử
dụng phương thức GET
để Kiểm tra trạng thái,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/rpa/task/execute</td><td>PATCH</td><td>Cập
nhật
cấu
hình</td><td>API /rpa/task/execute
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/network/qos/monitor</td><td>GET</td><td>Xóa
thông
tin</td><td>API
/network/qos/monitor
sử dụng phương thức
GET để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/network/qos/monitor</td><td>POST</td><td>Export
dữ
liệu</td><td>API
/network/qos/monitor
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr></tbody></table>

|<image_35>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/invoice/export</td><td>PUT</td><td>Xóa
thông
tin</td><td>API /invoice/export sử
dụng phương thức PUT
để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Có
versioning
v1/v2</td></tr><tr><td>/security/firewall/config</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API
/security/firewall/config
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/invoice/export</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /invoice/export sử
dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Có
versioning
v1/v2</td></tr><tr><td>/network/qos/monitor</td><td>DELETE</td><td>Export
dữ
liệu</td><td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/ivr/callflow</td><td>PATCH</td><td>Export
dữ
liệu</td><td>API /ivr/callflow sử
dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr></tbody></table>

|<image_36>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>PATCH</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Có
versioning
v1/v2</td></tr><tr><td>/ivr/callflow</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API /ivr/callflow sử
dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/ivr/callflow</td><td>PATCH</td><td>Xóa
thông
tin</td><td>API /ivr/callflow sử
dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/network/qos/monitor</td><td>DELETE</td><td>Xóa
thông
tin</td><td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/security/firewall/config</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao</td><td>Rollback
khi lỗi</td><td>Hỗ trợ
JSON và
XML</td></tr></tbody></table>

|<image_37>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/customer/update</td><td>DELETE</td><td>Xóa
thông
tin</td><td>API /customer/update
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Có
versioning
v1/v2</td></tr><tr><td>/network/qos/monitor</td><td>GET</td><td>Thêm
bản
ghi</td><td>API
/network/qos/monitor
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/crm/lead/import</td><td>DELETE</td><td>Export
dữ
liệu</td><td>API /crm/lead/import
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Có
versioning
v1/v2</td></tr><tr><td>/invoice/export</td><td>POST</td><td>Cập
nhật
cấu
hình</td><td>API /invoice/export sử
dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/security/firewall/config</td><td>GET</td><td>Export
dữ
liệu</td><td>API
/security/firewall/config
sử dụng phương thức
GET để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Giới hạn
rate-limit
1000
req/min</td></tr></tbody></table>

|<image_38>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/security/firewall/config</th><th>PATCH</th><th>Xóa
thông
tin</th><th>API
/security/firewall/config
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</th><th>Log đầy
đủ</th><th>Hỗ trợ
JSON và
XML</th></tr></thead><tbody><tr><td>/network/qos/monitor</td><td>POST</td><td>Export
dữ
liệu</td><td>API
/network/qos/monitor
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/rpa/task/execute</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API /rpa/task/execute
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Có
versioning
v1/v2</td></tr><tr><td>/crm/lead/import</td><td>PUT</td><td>Kiểm
tra
trạng
thái</td><td>API /crm/lead/import
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/invoice/export</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API /invoice/export sử
dụng phương thức PUT
để Thêm bản ghi, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr></tbody></table>

|<image_39>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/ivr/callflow</th><th>PATCH</th><th>Cập
nhật
cấu
hình</th><th>API /ivr/callflow sử
dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>Retry tối
đa 3 lần</th><th>Giới hạn
rate-limit
1000
req/min</th></tr></thead><tbody><tr><td>/network/qos/monitor</td><td>DELETE</td><td>Export
dữ
liệu</td><td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/customer/update</td><td>PUT</td><td>Xóa
thông
tin</td><td>API /customer/update
sử dụng phương thức
PUT để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/network/qos/monitor</td><td>PATCH</td><td>Xóa
thông
tin</td><td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/rpa/task/execute</td><td>POST</td><td>Xóa
thông
tin</td><td>API /rpa/task/execute
sử dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/crm/lead/import</td><td>PATCH</td><td>Xóa
thông</td><td>API /crm/lead/import
sử dụng phương thức</td><td>Thông
báo sự</td><td>Theo
chuẩn</td></tr></tbody></table>

|<image_40>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>tin</th><th>PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</th><th>kiện qua
Kafka</th><th>RESTful</th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>PATCH</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/customer/update</td><td>PUT</td><td>Xóa
thông
tin</td><td>API /customer/update
sử dụng phương thức
PUT để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/crm/lead/import</td><td>POST</td><td>Export
dữ
liệu</td><td>API /crm/lead/import
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/security/firewall/config</td><td>PATCH</td><td>Cập
nhật
cấu
hình</td><td>API
/security/firewall/config
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/rpa/task/execute</td><td>GET</td><td>Thêm
bản
ghi</td><td>API /rpa/task/execute
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr></tbody></table>

|<image_41>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log giao dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/network/qos/monitor</td><td>POST</td><td>Xóa
thông
tin</td><td>API
/network/qos/monitor
sử dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/customer/update</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API /customer/update
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/rpa/task/execute</td><td>PATCH</td><td>Cập
nhật
cấu
hình</td><td>API /rpa/task/execute
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API /crm/lead/import
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/invoice/export</td><td>GET</td><td>Xóa
thông
tin</td><td>API /invoice/export sử
dụng phương thức GET
để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/ivr/callflow</td><td>PUT</td><td>Export</td><td>API /ivr/callflow sử</td><td>Thông</td><td>Hỗ trợ</td></tr></tbody></table>

|<image_42>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>dữ
liệu</th><th>dụng phương thức PUT
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</th><th>báo sự
kiện qua
Kafka</th><th>JSON và
XML</th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>POST</td><td>Xóa
thông
tin</td><td>API /rpa/task/execute
sử dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/crm/lead/import</td><td>DELETE</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Có
versioning
v1/v2</td></tr><tr><td>/invoice/export</td><td>PATCH</td><td>Thêm
bản
ghi</td><td>API /invoice/export sử
dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/security/firewall/config</td><td>PUT</td><td>Cập
nhật
cấu
hình</td><td>API
/security/firewall/config
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/invoice/export</td><td>POST</td><td>Cập
nhật
cấu</td><td>API /invoice/export sử
dụng phương thức
POST để Cập nhật cấu</td><td>Thông
báo sự
kiện qua</td><td>Theo
chuẩn</td></tr></tbody></table>

|<image_43>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>hình</th><th>hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>Kafka</th><th>RESTful</th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>PUT</td><td>Kiểm
tra
trạng
thái</td><td>API /rpa/task/execute
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/network/qos/monitor</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API
/network/qos/monitor
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/security/firewall/config</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API
/security/firewall/config
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/crm/lead/import</td><td>PUT</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/security/firewall/config</td><td>GET</td><td>Export
dữ
liệu</td><td>API
/security/firewall/config
sử dụng phương thức
GET để Export dữ liệu,</td><td>Rollback
khi lỗi</td><td>Có
versioning
v1/v2</td></tr></tbody></table>

|<image_44>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>có xác thực OAuth2 và
log giao dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /rpa/task/execute
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/ivr/callflow</td><td>POST</td><td>Thêm
bản
ghi</td><td>API /ivr/callflow sử
dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/ivr/callflow</td><td>DELETE</td><td>Cập
nhật
cấu
hình</td><td>API /ivr/callflow sử
dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr><tr><td>/rpa/task/execute</td><td>DELETE</td><td>Export
dữ
liệu</td><td>API /rpa/task/execute
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/security/firewall/config</td><td>PUT</td><td>Export
dữ
liệu</td><td>API
/security/firewall/config
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr></tbody></table>

|<image_45>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log giao dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>POST</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/rpa/task/execute</td><td>PATCH</td><td>Xóa
thông
tin</td><td>API /rpa/task/execute
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/invoice/export</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /invoice/export sử
dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>GET</td><td>Cập
nhật
cấu
hình</td><td>API /crm/lead/import
sử dụng phương thức
GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/customer/update</td><td>GET</td><td>Kiểm
tra
trạng
thái</td><td>API /customer/update
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Hỗ trợ
JSON và
XML</td></tr></tbody></table>

|<image_46>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/rpa/task/execute</th><th>GET</th><th>Thêm
bản
ghi</th><th>API /rpa/task/execute
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</th><th>Rollback
khi lỗi</th><th>Theo
chuẩn
RESTful</th></tr></thead><tbody><tr><td>/invoice/export</td><td>GET</td><td>Kiểm
tra
trạng
thái</td><td>API /invoice/export sử
dụng phương thức GET
để Kiểm tra trạng thái,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr><tr><td>/invoice/export</td><td>PATCH</td><td>Thêm
bản
ghi</td><td>API /invoice/export sử
dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/invoice/export</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API /invoice/export sử
dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/security/firewall/config</td><td>DELETE</td><td>Cập
nhật
cấu
hình</td><td>API
/security/firewall/config
sử dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>PUT</td><td>Xóa
thông</td><td>API /invoice/export sử
dụng phương thức PUT</td><td>Retry tối</td><td>Theo
chuẩn</td></tr></tbody></table>

|<image_47>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>tin</th><th>để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</th><th>đa 3 lần</th><th>RESTful</th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>POST</td><td>Thêm
bản
ghi</td><td>API /crm/lead/import
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/network/qos/monitor</td><td>GET</td><td>Thêm
bản
ghi</td><td>API
/network/qos/monitor
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Có
versioning
v1/v2</td></tr><tr><td>/ivr/callflow</td><td>PUT</td><td>Cập
nhật
cấu
hình</td><td>API /ivr/callflow sử
dụng phương thức PUT
để Cập nhật cấu hình,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/rpa/task/execute</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /rpa/task/execute
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/rpa/task/execute</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API /rpa/task/execute
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr></tbody></table>

|<image_48>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log giao dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /crm/lead/import
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/customer/update</td><td>PATCH</td><td>Xóa
thông
tin</td><td>API /customer/update
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/ivr/callflow</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API /ivr/callflow sử
dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/network/qos/monitor</td><td>GET</td><td>Xóa
thông
tin</td><td>API
/network/qos/monitor
sử dụng phương thức
GET để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/crm/lead/import</td><td>DELETE</td><td>Xóa
thông
tin</td><td>API /crm/lead/import
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/ivr/callflow</td><td>PUT</td><td>Export</td><td>API /ivr/callflow sử</td><td>Retry tối</td><td>Theo</td></tr></tbody></table>

|<image_49>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>dữ
liệu</th><th>dụng phương thức PUT
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</th><th>đa 3 lần</th><th>chuẩn
RESTful</th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /rpa/task/execute
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/rpa/task/execute</td><td>PATCH</td><td>Export
dữ
liệu</td><td>API /rpa/task/execute
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/crm/lead/import</td><td>PUT</td><td>Xóa
thông
tin</td><td>API /crm/lead/import
sử dụng phương thức
PUT để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/rpa/task/execute</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /rpa/task/execute
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/crm/lead/import</td><td>GET</td><td>Export
dữ
liệu</td><td>API /crm/lead/import
sử dụng phương thức
GET để Export dữ liệu,
có xác thực OAuth2 và</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr></tbody></table>

|<image_50>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>log giao dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>DELETE</td><td>Export
dữ
liệu</td><td>API /rpa/task/execute
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/network/qos/monitor</td><td>PATCH</td><td>Thêm
bản
ghi</td><td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>GET</td><td>Export
dữ
liệu</td><td>API /invoice/export sử
dụng phương thức GET
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/rpa/task/execute</td><td>DELETE</td><td>Export
dữ
liệu</td><td>API /rpa/task/execute
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/security/firewall/config</td><td>PATCH</td><td>Xóa
thông
tin</td><td>API
/security/firewall/config
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr></tbody></table>

|<image_51>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>và log giao dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/customer/update</td><td>PUT</td><td>Cập
nhật
cấu
hình</td><td>API /customer/update
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>DELETE</td><td>Xóa
thông
tin</td><td>API /invoice/export sử
dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/customer/update</td><td>PUT</td><td>Export
dữ
liệu</td><td>API /customer/update
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/network/qos/monitor</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API
/network/qos/monitor
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/invoice/export</td><td>PUT</td><td>Xóa
thông
tin</td><td>API /invoice/export sử
dụng phương thức PUT
để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/network/qos/monitor</td><td>GET</td><td>Export</td><td>API</td><td>Retry tối</td><td>Tích hợp</td></tr></tbody></table>

|<image_52>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>dữ
liệu</th><th>/network/qos/monitor
sử dụng phương thức
GET để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</th><th>đa 3 lần</th><th>với API
Gateway</th></tr></thead><tbody><tr><td>/ivr/callflow</td><td>GET</td><td>Thêm
bản
ghi</td><td>API /ivr/callflow sử
dụng phương thức GET
để Thêm bản ghi, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/security/firewall/config</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/security/firewall/config</td><td>POST</td><td>Export
dữ
liệu</td><td>API
/security/firewall/config
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>POST</td><td>Export
dữ
liệu</td><td>API /invoice/export sử
dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr></tbody></table>

|<image_53>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/crm/lead/import</th><th>PATCH</th><th>Kiểm
tra
trạng
thái</th><th>API /crm/lead/import
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>Retry tối
đa 3 lần</th><th>Hỗ trợ
JSON và
XML</th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>PUT</td><td>Cập
nhật
cấu
hình</td><td>API /rpa/task/execute
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/invoice/export</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API /invoice/export sử
dụng phương thức PUT
để Thêm bản ghi, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API /crm/lead/import
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/ivr/callflow</td><td>PUT</td><td>Cập
nhật
cấu
hình</td><td>API /ivr/callflow sử
dụng phương thức PUT
để Cập nhật cấu hình,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/invoice/export</td><td>PATCH</td><td>Thêm
bản</td><td>API /invoice/export sử
dụng phương thức
PATCH để Thêm bản</td><td>Thành
công</td><td>Có
versioning</td></tr></tbody></table>

|<image_54>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>ghi</th><th>ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>&lt;1s</th><th>v1/v2</th></tr></thead><tbody><tr><td>/rpa/task/execute</td><td>PUT</td><td>Export
dữ
liệu</td><td>API /rpa/task/execute
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/invoice/export</td><td>DELETE</td><td>Thêm
bản
ghi</td><td>API /invoice/export sử
dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/invoice/export</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API /invoice/export sử
dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr><tr><td>/customer/update</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API /customer/update
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/rpa/task/execute</td><td>PATCH</td><td>Thêm
bản
ghi</td><td>API /rpa/task/execute
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr></tbody></table>

|<image_55>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/network/qos/monitor</td><td>PUT</td><td>Kiểm
tra
trạng
thái</td><td>API
/network/qos/monitor
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Có
versioning
v1/v2</td></tr><tr><td>/invoice/export</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /invoice/export sử
dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/ivr/callflow</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /ivr/callflow sử
dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/customer/update</td><td>PUT</td><td>Thêm
bản
ghi</td><td>API /customer/update
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Có
versioning
v1/v2</td></tr><tr><td>/rpa/task/execute</td><td>DELETE</td><td>Xóa
thông
tin</td><td>API /rpa/task/execute
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Log đầy
đủ</td><td>Tích hợp
với API
Gateway</td></tr></tbody></table>

|<image_56>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/crm/lead/import</th><th>DELETE</th><th>Thêm
bản
ghi</th><th>API /crm/lead/import
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>Retry tối
đa 3 lần</th><th>Giới hạn
rate-limit
1000
req/min</th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>PUT</td><td>Export
dữ
liệu</td><td>API /crm/lead/import
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/network/qos/monitor</td><td>POST</td><td>Export
dữ
liệu</td><td>API
/network/qos/monitor
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/security/firewall/config</td><td>POST</td><td>Kiểm
tra
trạng
thái</td><td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/ivr/callflow</td><td>PUT</td><td>Cập
nhật
cấu
hình</td><td>API /ivr/callflow sử
dụng phương thức PUT
để Cập nhật cấu hình,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Theo
chuẩn
RESTful</td></tr></tbody></table>

|<image_57>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>/crm/lead/import</th><th>DELETE</th><th>Cập
nhật
cấu
hình</th><th>API /crm/lead/import
sử dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>Retry tối
đa 3 lần</th><th>Tích hợp
với API
Gateway</th></tr></thead><tbody><tr><td>/ivr/callflow</td><td>DELETE</td><td>Cập
nhật
cấu
hình</td><td>API /ivr/callflow sử
dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/crm/lead/import</td><td>GET</td><td>Thêm
bản
ghi</td><td>API /crm/lead/import
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/security/firewall/config</td><td>PATCH</td><td>Export
dữ
liệu</td><td>API
/security/firewall/config
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr><tr><td>/ivr/callflow</td><td>PUT</td><td>Kiểm
tra
trạng
thái</td><td>API /ivr/callflow sử
dụng phương thức PUT
để Kiểm tra trạng thái,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Rollback
khi lỗi</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/network/qos/monitor</td><td>DELETE</td><td>Kiểm
tra</td><td>API
/network/qos/monitor</td><td>Rollback</td><td>Hỗ trợ
JSON và</td></tr></tbody></table>

|<image_58>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>trạng
thái</th><th>sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th>khi lỗi</th><th>XML</th></tr></thead><tbody><tr><td>/invoice/export</td><td>DELETE</td><td>Xóa
thông
tin</td><td>API /invoice/export sử
dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/network/qos/monitor</td><td>POST</td><td>Thêm
bản
ghi</td><td>API
/network/qos/monitor
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/security/firewall/config</td><td>DELETE</td><td>Xóa
thông
tin</td><td>API
/security/firewall/config
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/invoice/export</td><td>DELETE</td><td>Cập
nhật
cấu
hình</td><td>API /invoice/export sử
dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/customer/update</td><td>PATCH</td><td>Xóa
thông</td><td>API /customer/update
sử dụng phương thức</td><td>Rollback</td><td>Tích hợp
với API</td></tr></tbody></table>

|<image_59>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>tin</th><th>PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</th><th>khi lỗi</th><th>Gateway</th></tr></thead><tbody><tr><td>/ivr/callflow</td><td>POST</td><td>Cập
nhật
cấu
hình</td><td>API /ivr/callflow sử
dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/security/firewall/config</td><td>DELETE</td><td>Cập
nhật
cấu
hình</td><td>API
/security/firewall/config
sử dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/customer/update</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /customer/update
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/customer/update</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /customer/update
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Theo
chuẩn
RESTful</td></tr><tr><td>/security/firewall/config</td><td>POST</td><td>Export
dữ</td><td>API
/security/firewall/config
sử dụng phương thức</td><td>Log đầy
đủ</td><td>Tích hợp
với API</td></tr></tbody></table>

|<image_60>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th>liệu</th><th>POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</th><th></th><th>Gateway</th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>DELETE</td><td>Kiểm
tra
trạng
thái</td><td>API /crm/lead/import
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Hỗ trợ
JSON và
XML</td></tr><tr><td>/crm/lead/import</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /crm/lead/import
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Log đầy
đủ</td><td>Có
versioning
v1/v2</td></tr><tr><td>/customer/update</td><td>PUT</td><td>Export
dữ
liệu</td><td>API /customer/update
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/invoice/export</td><td>GET</td><td>Export
dữ
liệu</td><td>API /invoice/export sử
dụng phương thức GET
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td><td>Thông
báo sự
kiện qua
Kafka</td><td>Giới hạn
rate-limit
1000
req/min</td></tr><tr><td>/customer/update</td><td>POST</td><td>Thêm
bản
ghi</td><td>API /customer/update
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao</td><td>Retry tối
đa 3 lần</td><td>Hỗ trợ
JSON và
XML</td></tr></tbody></table>

|<image_61>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD448</th></tr></thead><tbody><tr><td></td><td>QUẢN LÝ API &amp; LOG</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th></th><th></th><th>dịch chi tiết.</th><th></th><th></th></tr></thead><tbody><tr><td>/crm/lead/import</td><td>DELETE</td><td>Xóa
thông
tin</td><td>API /crm/lead/import
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Có
versioning
v1/v2</td></tr><tr><td>/rpa/task/execute</td><td>GET</td><td>Thêm
bản
ghi</td><td>API /rpa/task/execute
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Có
versioning
v1/v2</td></tr><tr><td>/ivr/callflow</td><td>POST</td><td>Thêm
bản
ghi</td><td>API /ivr/callflow sử
dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Retry tối
đa 3 lần</td><td>Tích hợp
với API
Gateway</td></tr><tr><td>/customer/update</td><td>PATCH</td><td>Kiểm
tra
trạng
thái</td><td>API /customer/update
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td><td>Thành
công
&lt;1s</td><td>Hỗ trợ
JSON và
XML</td></tr></tbody></table>

|<image_62>|



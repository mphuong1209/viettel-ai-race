# Public_447

<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Test case</th><th>Mô tả</th><th>Input</th><th></th><th>Expected</th><th></th><th></th><th>Phương</th><th></th><th>Ghi chú</th></tr></thead><tbody><tr><td></td><td></td><td></td><td></td><td>Output</td><td></td><td></td><td>pháp</td><td></td><td></td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>API call
batch
1000
request</td><td>User
login
thành
công
trong &lt;1s</td><td></td><td></td><td>JMeter
script</td><td></td><td></td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td></td><td></td><td>Manual test
plan</td><td></td><td></td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td></td><td></td><td>Manual test
plan</td><td></td><td></td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Cluster
failover
tự động
trong 5s</td><td></td><td></td><td>Manual test
plan</td><td></td><td></td><td>Theo chuẩn
ISTQB</td></tr></tbody></table>

|<image_1>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Security
scan</th><th>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th>API call
batch
1000
request</th><th>User
login
thành
công
trong &lt;1s</th><th>Manual test
plan</th><th>Gửi báo cáo
PDF hàng ngày</th></tr></thead><tbody><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr></tbody></table>

|<image_2>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>bao gồm kịch bản
thành công và thất
bại.</th><th></th><th>sự cố</th><th></th><th></th></tr></thead><tbody><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr></tbody></table>

|<image_3>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>API stress
test</th><th>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th>invalid
data</th><th>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</th><th>Automation
Selenium</th><th>Phải log toàn
bộ kết quả</th></tr></thead><tbody><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>network
disconnect</td><td>Cluster
failover
tự động
trong 5s</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>User
login
thành
công
trong &lt;1s</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Kịch bản
Ansible</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản</td><td>network
disconnect</td><td>User
login
thành
công</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr></tbody></table>

|<image_4>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>thành công và thất
bại.</th><th></th><th>trong &lt;1s</th><th></th><th></th></tr></thead><tbody><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>Cluster
failover
tự động
trong 5s</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>API stress</td><td>Thực hiện API stress
test để kiểm thử</td><td>invalid</td><td>User
login</td><td>JMeter</td><td>Gửi báo cáo</td></tr></tbody></table>

|<image_5>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>test</th><th>chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th>data</th><th>thành
công
trong &lt;1s</th><th>script</th><th>PDF hàng ngày</th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>invalid
data</td><td>Cluster
failover
tự động
trong 5s</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Cluster
failover
tự động
trong 5s</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành</td><td>invalid
data</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>Theo chuẩn
ISTQB</td></tr></tbody></table>

|<image_6>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>công và thất bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ</td><td>network
disconnect</td><td>Hệ thống
chịu tải
20k TPS
không</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr></tbody></table>

|<image_7>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>thống, bao gồm kịch
bản thành công và
thất bại.</th><th></th><th>gián đoạn</th><th></th><th></th></tr></thead><tbody><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>DB
corruption</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>DB
corruption</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>JMeter
script</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Database</td><td>Thực hiện Database</td><td>DB</td><td>Hệ thống</td><td>Automation</td><td>So sánh</td></tr></tbody></table>

|<image_8>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>recovery
test</th><th>recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</th><th>corruption</th><th>chịu tải
20k TPS
không
gián đoạn</th><th>Selenium</th><th>benchmark với
release trước</th></tr></thead><tbody><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>Cluster
failover
tự động
trong 5s</td><td>Automation
Selenium</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch</td><td>invalid
data</td><td>User
login
thành
công</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr></tbody></table>

|<image_9>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>bản thành công và
thất bại.</th><th></th><th>trong &lt;1s</th><th></th><th></th></tr></thead><tbody><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>invalid
data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Manual test
plan</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr></tbody></table>

|<image_10>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>thống, bao gồm kịch
bản thành công và
thất bại.</th><th></th><th>sự cố</th><th></th><th></th></tr></thead><tbody><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>network
disconnect</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>API stress</td><td>Thực hiện API stress</td><td>network</td><td>Không</td><td>JMeter</td><td>Theo chuẩn</td></tr></tbody></table>

|<image_11>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>test</th><th>test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th>disconnect</th><th>phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</th><th>script</th><th>ISTQB</th></tr></thead><tbody><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>invalid
data</td><td>Cluster
failover
tự động
trong 5s</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch</td><td>invalid
data</td><td>Cluster
failover
tự động
trong 5s</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr></tbody></table>

|<image_12>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>bản thành công và
thất bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>DB
corruption</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>Cluster
failover
tự động
trong 5s</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Data
consistency</td><td>Thực hiện Data
consistency test để</td><td>network</td><td>Hệ thống
chịu tải</td><td>Manual test</td><td>Phải log toàn</td></tr></tbody></table>

|<image_13>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>test</th><th>kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</th><th>disconnect</th><th>20k TPS
không
gián đoạn</th><th>plan</th><th>bộ kết quả</th></tr></thead><tbody><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Cluster
failover
tự động
trong 5s</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Cluster
failover
tự động
trong 5s</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>invalid
data</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Automation
Selenium</td><td>Theo chuẩn
ISTQB</td></tr></tbody></table>

|<image_14>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Load test</th><th>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>network
disconnect</th><th>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</th><th>JMeter
script</th><th>Gửi báo cáo
PDF hàng ngày</th></tr></thead><tbody><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Automation
Selenium</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất</td><td>stress load
&gt; 10k
TPS</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Theo chuẩn
ISTQB</td></tr></tbody></table>

|<image_15>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>DB
corruption</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Automation
Selenium</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Cluster
failover
tự động
trong 5s</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Security</td><td>Thực hiện Security
scan để kiểm thử</td><td>valid data</td><td>Dữ liệu
được khôi</td><td>Manual test</td><td>Test môi
trường Pre-</td></tr></tbody></table>

|<image_16>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>scan</th><th>chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th></th><th>phục toàn
vẹn sau
sự cố</th><th>plan</th><th>Prod</th></tr></thead><tbody><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>DB
corruption</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>DB
corruption</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr></tbody></table>

|<image_17>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Failover
test</th><th>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th>DB
corruption</th><th>User
login
thành
công
trong &lt;1s</th><th>Manual test
plan</th><th>Test môi
trường Pre-
Prod</th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>Cluster
failover
tự động
trong 5s</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr></tbody></table>

|<image_18>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>công và thất bại.</th><th></th><th>sự cố</th><th></th><th></th></tr></thead><tbody><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Database
recovery</td><td>Thực hiện Database
recovery test để</td><td>valid data</td><td>User
login</td><td>JMeter</td><td>Theo chuẩn</td></tr></tbody></table>

|<image_19>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>test</th><th>kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</th><th></th><th>thành
công
trong &lt;1s</th><th>script</th><th>ISTQB</th></tr></thead><tbody><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr></tbody></table>

|<image_20>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Failover
test</th><th>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th>DB
corruption</th><th>Cluster
failover
tự động
trong 5s</th><th>Automation
Selenium</th><th>Gửi báo cáo
PDF hàng ngày</th></tr></thead><tbody><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>User
login
thành
công
trong &lt;1s</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,</td><td>valid data</td><td>User
login
thành
công</td><td>Automation
Selenium</td><td>Theo chuẩn
ISTQB</td></tr></tbody></table>

|<image_21>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>bao gồm kịch bản
thành công và thất
bại.</th><th></th><th>trong &lt;1s</th><th></th><th></th></tr></thead><tbody><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Data</td><td>Thực hiện Data</td><td>DB</td><td>User</td><td>Kịch bản</td><td>Test môi</td></tr></tbody></table>

|<image_22>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>consistency
test</th><th>consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</th><th>corruption</th><th>login
thành
công
trong &lt;1s</th><th>Ansible</th><th>trường Pre-
Prod</th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành</td><td>network
disconnect</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr></tbody></table>

|<image_23>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>công và thất bại.</th><th></th><th>Top 10</th><th></th><th></th></tr></thead><tbody><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>DB
corruption</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành</td><td>valid data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr></tbody></table>

|<image_24>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>công và thất bại.</th><th></th><th>Top 10</th><th></th><th></th></tr></thead><tbody><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>invalid
data</td><td>Cluster
failover
tự động
trong 5s</td><td>Automation
Selenium</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr></tbody></table>

|<image_25>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>gồm kịch bản thành
công và thất bại.</th><th></th><th>trong &lt;1s</th><th></th><th></th></tr></thead><tbody><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>DB
corruption</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>DB
corruption</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng</td><td>stress load
&gt; 10k</td><td>Không
phát hiện
lỗ hổng</td><td>JMeter
script</td><td>So sánh
benchmark với</td></tr></tbody></table>

|<image_26>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>TPS</th><th>bảo mật
OWASP
Top 10</th><th></th><th>release trước</th></tr></thead><tbody><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>User
login
thành
công
trong &lt;1s</td><td>JMeter
script</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Data</td><td>Thực hiện Data</td><td>invalid</td><td>User</td><td>Automation</td><td>So sánh</td></tr></tbody></table>

|<image_27>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>consistency
test</th><th>consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</th><th>data</th><th>login
thành
công
trong &lt;1s</th><th>Selenium</th><th>benchmark với
release trước</th></tr></thead><tbody><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>invalid
data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Automation
Selenium</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành</td><td>stress load
&gt; 10k
TPS</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr></tbody></table>

|<image_28>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>công và thất bại.</th><th></th><th>Top 10</th><th></th><th></th></tr></thead><tbody><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Cluster
failover
tự động
trong 5s</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Cluster
failover
tự động
trong 5s</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Database
recovery</td><td>Thực hiện Database
recovery test để</td><td>network</td><td>Cluster
failover</td><td>Manual test</td><td>So sánh
benchmark với</td></tr></tbody></table>

|<image_29>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>test</th><th>kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</th><th>disconnect</th><th>tự động
trong 5s</th><th>plan</th><th>release trước</th></tr></thead><tbody><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Cluster
failover
tự động
trong 5s</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Automation
Selenium</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr></tbody></table>

|<image_30>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>User
login
thành
công
trong &lt;1s</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>JMeter
script</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn</td><td>JMeter
script</td><td>Test môi
trường Pre-</td></tr></tbody></table>

|<image_31>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th></th><th>vẹn sau
sự cố</th><th></th><th>Prod</th></tr></thead><tbody><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Cluster
failover
tự động
trong 5s</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Data
consistency</td><td>Thực hiện Data
consistency test để</td><td>API call
batch</td><td>Không
phát hiện</td><td>Kịch bản</td><td>Theo chuẩn</td></tr></tbody></table>

|<image_32>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>test</th><th>kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</th><th>1000
request</th><th>lỗ hổng
bảo mật
OWASP
Top 10</th><th>Ansible</th><th>ISTQB</th></tr></thead><tbody><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Manual test
plan</td><td>Theo chuẩn
ISTQB</td></tr></tbody></table>

|<image_33>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Data
consistency
test</th><th>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</th><th>stress load
&gt; 10k
TPS</th><th>Hệ thống
chịu tải
20k TPS
không
gián đoạn</th><th>Kịch bản
Ansible</th><th>Phải log toàn
bộ kết quả</th></tr></thead><tbody><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>invalid
data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr></tbody></table>

|<image_34>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>bản thành công và
thất bại.</th><th></th><th>sự cố</th><th></th><th></th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>API call
batch
1000
request</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>User
login
thành
công
trong &lt;1s</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Failover</td><td>Thực hiện Failover
test để kiểm thử</td><td>DB</td><td>Không
phát hiện</td><td>Automation</td><td>Theo chuẩn</td></tr></tbody></table>

|<image_35>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>test</th><th>chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th>corruption</th><th>lỗ hổng
bảo mật
OWASP
Top 10</th><th>Selenium</th><th>ISTQB</th></tr></thead><tbody><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Automation
Selenium</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Cluster
failover
tự động
trong 5s</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất</td><td>network
disconnect</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr></tbody></table>

|<image_36>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>User
login
thành
công
trong &lt;1s</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Database
recovery</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-</td></tr></tbody></table>

|<image_37>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>test</th><th>và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</th><th></th><th>vẹn sau
sự cố</th><th></th><th>Prod</th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>network
disconnect</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Test môi
trường Pre-
Prod</td></tr></tbody></table>

|<image_38>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Load test</th><th>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>valid data</th><th>Hệ thống
chịu tải
20k TPS
không
gián đoạn</th><th>Automation
Selenium</th><th>Gửi báo cáo
PDF hàng ngày</th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành</td><td>stress load
&gt; 10k
TPS</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr></tbody></table>

|<image_39>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>công và thất bại.</th><th></th><th>Top 10</th><th></th><th></th></tr></thead><tbody><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>invalid
data</td><td>User
login
thành
công
trong &lt;1s</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu</td><td>network
disconnect</td><td>Cluster
failover
tự động</td><td>Manual test
plan</td><td>So sánh
benchmark với</td></tr></tbody></table>

|<image_40>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th></th><th>trong 5s</th><th></th><th>release trước</th></tr></thead><tbody><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>invalid
data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và</td><td>API call
batch
1000
request</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr></tbody></table>

|<image_41>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>thất bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Security</td><td>Thực hiện Security
scan để kiểm thử</td><td>invalid</td><td>Hệ thống
chịu tải</td><td>Kịch bản</td><td>Test môi
trường Pre-</td></tr></tbody></table>

|<image_42>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>scan</th><th>chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th>data</th><th>20k TPS
không
gián đoạn</th><th>Ansible</th><th>Prod</th></tr></thead><tbody><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và</td><td>network
disconnect</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr></tbody></table>

|<image_43>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>thất bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>DB
corruption</td><td>Cluster
failover
tự động
trong 5s</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ</td><td>valid data</td><td>User
login
thành
công</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr></tbody></table>

|<image_44>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>thống, bao gồm kịch
bản thành công và
thất bại.</th><th></th><th>trong &lt;1s</th><th></th><th></th></tr></thead><tbody><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Theo chuẩn
ISTQB</td></tr></tbody></table>

|<image_45>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Login test</th><th>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>DB
corruption</th><th>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</th><th>Manual test
plan</th><th>So sánh
benchmark với
release trước</th></tr></thead><tbody><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>DB
corruption</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Automation
Selenium</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Cluster
failover
tự động
trong 5s</td><td>Automation
Selenium</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành</td><td>invalid
data</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>Phải log toàn
bộ kết quả</td></tr></tbody></table>

|<image_46>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>công và thất bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng</td><td>stress load
&gt; 10k</td><td>User
login
thành</td><td>JMeter
script</td><td>So sánh
benchmark với</td></tr></tbody></table>

|<image_47>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>TPS</th><th>công
trong &lt;1s</th><th></th><th>release trước</th></tr></thead><tbody><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Cluster
failover
tự động
trong 5s</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>DB
corruption</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Kịch bản
Ansible</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr></tbody></table>

|<image_48>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Load test</th><th>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>stress load
&gt; 10k
TPS</th><th>Hệ thống
chịu tải
20k TPS
không
gián đoạn</th><th>JMeter
script</th><th>Theo chuẩn
ISTQB</th></tr></thead><tbody><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>API call
batch
1000
request</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr></tbody></table>

|<image_49>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>thất bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu</td><td>API call
batch
1000</td><td>User
login
thành</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr></tbody></table>

|<image_50>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th>request</th><th>công
trong &lt;1s</th><th></th><th></th></tr></thead><tbody><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>Cluster
failover
tự động
trong 5s</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr></tbody></table>

|<image_51>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Load test</th><th>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>network
disconnect</th><th>Cluster
failover
tự động
trong 5s</th><th>Manual test
plan</th><th>Gửi báo cáo
PDF hàng ngày</th></tr></thead><tbody><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất</td><td>invalid
data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr></tbody></table>

|<image_52>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Cluster
failover
tự động
trong 5s</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>DB
corruption</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Automation
Selenium</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức</td><td>stress load
&gt; 10k</td><td>Hệ thống
chịu tải</td><td>Automation</td><td>Phải log toàn</td></tr></tbody></table>

|<image_53>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>TPS</th><th>20k TPS
không
gián đoạn</th><th>Selenium</th><th>bộ kết quả</th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>DB
corruption</td><td>Cluster
failover
tự động
trong 5s</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Cluster
failover
tự động
trong 5s</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr></tbody></table>

|<image_54>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Login test</th><th>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>stress load
&gt; 10k
TPS</th><th>Hệ thống
chịu tải
20k TPS
không
gián đoạn</th><th>JMeter
script</th><th>Phải log toàn
bộ kết quả</th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Automation
Selenium</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và</td><td>invalid
data</td><td>Cluster
failover
tự động
trong 5s</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr></tbody></table>

|<image_55>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>thất bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Manual test
plan</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức</td><td>invalid</td><td>Hệ thống
chịu tải</td><td>Kịch bản</td><td>Phải log toàn</td></tr></tbody></table>

|<image_56>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>data</th><th>20k TPS
không
gián đoạn</th><th>Ansible</th><th>bộ kết quả</th></tr></thead><tbody><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>DB
corruption</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>network
disconnect</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr></tbody></table>

|<image_57>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Login test</th><th>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>network
disconnect</th><th>User
login
thành
công
trong &lt;1s</th><th>JMeter
script</th><th>Gửi báo cáo
PDF hàng ngày</th></tr></thead><tbody><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Cluster
failover
tự động
trong 5s</td><td>Automation
Selenium</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản</td><td>invalid
data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr></tbody></table>

|<image_58>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>thành công và thất
bại.</th><th></th><th>Top 10</th><th></th><th></th></tr></thead><tbody><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức</td><td>API call
batch</td><td>Cluster
failover</td><td>Kịch bản</td><td>So sánh
benchmark với</td></tr></tbody></table>

|<image_59>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>1000
request</th><th>tự động
trong 5s</th><th>Ansible</th><th>release trước</th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>network
disconnect</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và</td><td>network
disconnect</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr></tbody></table>

|<image_60>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>thất bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>invalid
data</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Kịch bản
Ansible</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu</td><td>valid data</td><td>Không
phát hiện
lỗ hổng</td><td>Manual test
plan</td><td>So sánh
benchmark với</td></tr></tbody></table>

|<image_61>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th></th><th>bảo mật
OWASP
Top 10</th><th></th><th>release trước</th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>invalid
data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>JMeter
script</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và</td><td>network
disconnect</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr></tbody></table>

|<image_62>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>thất bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Cluster
failover
tự động
trong 5s</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>invalid
data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Security</td><td>Thực hiện Security
scan để kiểm thử</td><td>API call
batch</td><td>Hệ thống
chịu tải</td><td>Manual test</td><td>So sánh
benchmark với</td></tr></tbody></table>

|<image_63>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>scan</th><th>chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th>1000
request</th><th>20k TPS
không
gián đoạn</th><th>plan</th><th>release trước</th></tr></thead><tbody><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Manual test
plan</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>DB
corruption</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>API stress</td><td>Thực hiện API stress</td><td>invalid</td><td>Không</td><td>Kịch bản</td><td>Gửi báo cáo</td></tr></tbody></table>

|<image_64>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>test</th><th>test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</th><th>data</th><th>phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</th><th>Ansible</th><th>PDF hàng ngày</th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>Cluster
failover
tự động
trong 5s</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>network
disconnect</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Automation
Selenium</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Data
consistency
test</td><td>Thực hiện Data
consistency test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và</td><td>valid data</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr></tbody></table>

|<image_65>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>thất bại.</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>invalid
data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>JMeter
script</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>DB
corruption</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>DB
corruption</td><td>Cluster
failover
tự động
trong 5s</td><td>JMeter
script</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Cluster
failover
tự động
trong 5s</td><td>Automation
Selenium</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất</td><td>invalid
data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr></tbody></table>

|<image_66>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th></th><th>bại.</th><th></th><th>Top 10</th><th></th><th></th></tr></thead><tbody><tr><td>Security
scan</td><td>Thực hiện Security
scan để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>So sánh
benchmark với
release trước</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>DB
corruption</td><td>User
login
thành
công
trong &lt;1s</td><td>Manual test
plan</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Cluster
failover
tự động
trong 5s</td><td>Automation
Selenium</td><td>Gửi báo cáo
PDF hàng ngày</td></tr><tr><td>Database
recovery</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng</td><td>valid data</td><td>Cluster
failover
tự động</td><td>Kịch bản
Ansible</td><td>Gửi báo cáo
PDF hàng ngày</td></tr></tbody></table>

|<image_67>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>test</th><th>và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</th><th></th><th>trong 5s</th><th></th><th></th></tr></thead><tbody><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>API call
batch
1000
request</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>Kịch bản
Ansible</td><td>Test môi
trường Pre-
Prod</td></tr><tr><td>Database
recovery
test</td><td>Thực hiện Database
recovery test để
kiểm thử chức năng
và hiệu năng của hệ
thống, bao gồm kịch
bản thành công và
thất bại.</td><td>stress load
&gt; 10k
TPS</td><td>User
login
thành
công
trong &lt;1s</td><td>Kịch bản
Ansible</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Load test</td><td>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Manual test
plan</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>API stress
test</td><td>Thực hiện API stress
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>stress load
&gt; 10k
TPS</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Manual test
plan</td><td>Gửi báo cáo
PDF hàng ngày</td></tr></tbody></table>

|<image_68>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

<table><thead><tr><th>Load test</th><th>Thực hiện Load test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</th><th>invalid
data</th><th>User
login
thành
công
trong &lt;1s</th><th>Kịch bản
Ansible</th><th>Theo chuẩn
ISTQB</th></tr></thead><tbody><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Hệ thống
chịu tải
20k TPS
không
gián đoạn</td><td>Kịch bản
Ansible</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>valid data</td><td>Không
phát hiện
lỗ hổng
bảo mật
OWASP
Top 10</td><td>Kịch bản
Ansible</td><td>Theo chuẩn
ISTQB</td></tr><tr><td>Failover
test</td><td>Thực hiện Failover
test để kiểm thử
chức năng và hiệu
năng của hệ thống,
bao gồm kịch bản
thành công và thất
bại.</td><td>network
disconnect</td><td>Dữ liệu
được khôi
phục toàn
vẹn sau
sự cố</td><td>JMeter
script</td><td>Phải log toàn
bộ kết quả</td></tr><tr><td>Login test</td><td>Thực hiện Login test
để kiểm thử chức
năng và hiệu năng
của hệ thống, bao
gồm kịch bản thành
công và thất bại.</td><td>network
disconnect</td><td>User
login
thành
công
trong &lt;1s</td><td>Automation
Selenium</td><td>Theo chuẩn
ISTQB</td></tr></tbody></table>

|<image_69>|


<table><thead><tr><th></th><th>VIETTEL AI RACE</th><th>TD447</th></tr></thead><tbody><tr><td></td><td>KỊCH BẢN KIỂM THỬ QA</td><td>Lần ban hành: 1</td></tr></tbody></table>

|<image_70>|



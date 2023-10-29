# Datatable in image to Text
Đây là đồ án môn học Computer Vision của nhóm 5. Nghiên cứu về chuyển đổi dữ liệu ở dạng bảng ở trên hình ảnh thành file excel.

## Members
1. Nguyễn Anh Tuấn (trưởng nhóm)
2. Nguyễn Bảo Chung
3. Trần Bách Khoa
4. Tống Duy Ngọc Nam
5. Lê Thành Nhân

## Install
Để có thể thực hiện được demo thì mình phải thực hiện việc cài đặt như sau:
1. Với GUI (dùng VSCode):
 - Dùng với extension (VSCode Extension) Live Server của Ritwick Dey.
2. Với API (NodeJS):
 - Phải cài Node >= v18.15.0 (npm sẽ được tự động cài).
 - Mở terminal trong thư mục nodejs và gõ `npm i` thì sẽ tự động cài các packages cần thiết.
3. Với Python
 - Cài python trong máy >= v3.9.0
 - Cài numpy, cv2.
 - Cài pytorch [ở đây](https://pytorch.org/)

## Startup
Khởi động thì mình chỉ cần khởi động GUI và API, chương trình python sẽ được API sử dụng trong quá trình demo.
1. Với GUI (dùng VSCode): thì ấn vào nút `Go Live` ở góc bên phải của màn hình. Nếu như nó hiện lên cây thư mục như là gui, nodejs, python thì có nghĩa là nó đang mở ở root dir, nên mình phải bấm vào trong `gui`. Nhớ là phải vào `gui` trước khi bật `Go Live`.
2. Với API: mở terminal trong folder `nodejs` và gõ `npm run dev`. Đợi một lúc ứng dụng API sẽ khởi động.
3. Với Python Programs: tải các file xml cần thiết, haarcascade_eye_tree_eyeglasses và haarcascade_frontalface_default.

## About
Repo này là một phần của đồ án môn học, và nhằm hỗ trợ tốt nhất cho việc demo thì nhóm quyết định chia phần demo thành 2 ứng dụng khác nhau là GUI và API và 1 chương trình Python.

Với ý tưởng là người dùng sẽ input vào từ GUI cùng với một số thông tin (nếu có) -> Ứng dụng API sẽ xử lý các thông tin và dùng tiến trình con để "nhờ" chương trình Python tính toán tiếp phần này -> Sau khi xử lý xong thì gửi dữ liệu về cho GUI.

Chương trình python sẽ có thể bao gồm 1 hoặc nhiều chương trình con trong đó dưới dạng script dùng để thực hiện 1 hoặc nhiều các công việc cụ thể trong phần demo.
![image](https://github.com/NguyenAnhTuan1912/datatable-image-to-text/assets/86825061/0efff10f-97e6-4d29-b6f5-add35c27a38d)

Trong mỗi phần của repo (folder gui, nodejs và python) sẽ được nói rõ hơn.

## Test
Để test một số tính năng như là làm mờ ảnh, chuyển ảnh màu thành ảnh xám và nhận diện khuôn mặt. Mục đích test là để trực quan cách javascript và python làm việc với nhau, cũng như là cách mà ứng dụng nó hoạt động.

Khởi động dự án như hướng dẫn phía trên. Khi khởi động GUI, thì sẽ vào trang chủ (trang này sẽ là nơi demo chính của ứng dụng)
![image](https://github.com/NguyenAnhTuan1912/datatable-image-to-text/assets/86825061/54f7811b-02c6-4283-a95e-4609178ab737)

Ấn vào __Chuyển qua Test section__. Tiếp theo mình sẽ chuyển tới Test Section
![image](https://github.com/NguyenAnhTuan1912/datatable-image-to-text/assets/86825061/8bed1104-5ad5-41e9-bc51-6096866c1567)

Mình có thể thấy có 3 tính năng chính.
- Làm mờ ảnh
- Đổi hệ màu
- Nhận diện khuôn mặt

### Làm mờ ảnh
__Hướng dẫn__
Làm mờ ảnh có một thông số là Blur Strength, độ mạnh của mờ. Càng cao thì ảnh càng mờ, thông số này được giới hạn trong khoảng `[1, 20]`
1. Ấn vào <strong>Choose File</strong>.
2. Chọn một tấm ảnh muốn làm mờ.
3. Chọn độ mạnh của blur và ấn __Làm mờ__.
![image](https://github.com/NguyenAnhTuan1912/datatable-image-to-text/assets/86825061/112cd71b-cd0e-4539-bf69-735b0e7f681a)
4. Chờ Backend thực thi. Sau khi thực thi xong thì sẽ có một popup Download hiện lên, lưu ảnh vào đâu đó.
5. Mở ảnh trong folder vừa lưu và xem kết quả.

### Đổi hệ màu
__Hướng dẫn__
Đổi màu ảnh đơn giản, chọn một select bên dưới để chọn một hệ màu khác.
1. Ấn vào __Choose File__
2. Chọn một tấm ảnh muốn đổi màu.
3. Chọn hệ màu muốn đối và ấn __Đổi màu__.
![image](https://github.com/NguyenAnhTuan1912/datatable-image-to-text/assets/86825061/79f7f88a-f065-4278-999a-c3a15f0087b4)
5. Chờ Backend thực thi. Sau khi thực thi xong thì sẽ có một popup Download hiện lên, lưu ảnh vào đâu đó.
6. Mở ảnh trong folder vừa lưu và xem kết quả.
![image](https://github.com/NguyenAnhTuan1912/datatable-image-to-text/assets/86825061/57672b1d-9e7e-4881-9997-2da775007651)

### Nhận diện khuôn mặt
__Hướng dẫn__
Nhận diện khuôn mặt với thuật toán haarcascade (OpenCV)
1. Ấn vào __Choose File__
2. Chọn một tấm ảnh có mặt người.
3. Điều chỉnh Scale Factor và Min Neighbors sau đó ấn __Nhận diện__.
![image](https://github.com/NguyenAnhTuan1912/datatable-image-to-text/assets/86825061/0682f3d8-8731-46cd-a912-eb5f12f5f9e7)
5. Chờ Backend thực thi. Sau khi thực thi xong thì sẽ có một popup Download hiện lên, lưu ảnh vào đâu đó.
6. Mở ảnh trong folder vừa lưu và xem kết quả.
![image](https://github.com/NguyenAnhTuan1912/datatable-image-to-text/assets/86825061/3dce7203-01cd-4930-b635-af04ba711ff9)

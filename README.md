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
1. Với GUI (dùng VSCode): thì ấn vào nút `Go Live` ở góc bên phải của màn hình. Nếu như nó hiện lên cây thư mục như là gui, nodejs, python thì có nghĩa là nó đang mở ở root dir, nên mình phải bấm vào trong `gui`.
2. Với API: mở terminal trong folder `nodejs` và gõ `npm run dev`. Đợi một lúc ứng dụng API sẽ khởi động.

## About
Repo này là một phần của đồ án môn học, và nhằm hỗ trợ tốt nhất cho việc demo thì nhóm quyết định chia phần demo thành 2 ứng dụng khác nhau là GUI và API và 1 chương trình Python.

Với ý tưởng là người dùng sẽ input vào từ GUI cùng với một số thông tin (nếu có) -> Ứng dụng API sẽ xử lý các thông tin và dùng tiến trình con để "nhờ" chương trình Python tính toán tiếp phần này -> Sau khi xử lý xong thì gửi dữ liệu về cho GUI.

Chương trình python sẽ có thể bao gồm 1 hoặc nhiều chương trình con trong đó dưới dạng script dùng để thực hiện 1 hoặc nhiều các công việc cụ thể trong phần demo.

Trong mỗi phần của repo (folder gui, nodejs và python) sẽ được nói rõ hơn.

## Test
Vào đường dẫn
```
/gui/test.html
```
Để test một số tính năng như là làm mờ ảnh, chuyển ảnh màu thành ảnh xám và nhận diện khuôn mặt.
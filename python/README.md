# DIITT Python Programs
Chương trình Python bao gồm các chương trình con dùng để thực hiện một số nhiệm vụ, công việc được "nhờ" từ ứng dụng API.

## Tech stack
1. Python
2. Pytorch
3. Numpy, OpenCV

## About
Chương trình Python được xây dựng bằng Python cùng với Pytorch cùng với một số mô hình Neuron khác và các thư viện khác như numpy, cv2 (open-cv). Để thực hiện một hay nhiều nhiệm vụ từ ứng dụng API.

Lấy dữ liệu của ảnh cùng một số thông tin được gửi về từ ứng dụng API, từ đó chương trình python sẽ chịu trách nhiệm xử lý và tính toán các thông tin này. Sau đó là gửi lại dữ liệu cho ứng dụng API.

Phục vụ cho việc test, thì ứng dụng API sẽ hỗ trợ một số thứ sau:
- Làm mờ ảnh.
- Chuyển đổi ảnh màu thành xám.
- Nhận diện khuôn mặt trong ảnh.

Folder `test` sẽ chứa các script test chính của app. Còn các script như là `blur_image.py`, `change_color_image.py` và `face_recognition.py` là những script dùng với product, nhưng chỉ là những chức năng TEST (test này khác với test trong folder `test`, anh em lưu ý)

# Installation
Một số thứ yêu cầu phải được cài đặt

```
opencv-python
numpy
matplotlib
pytesseract
```

Có một thư mục tên là `builds`. Thư mục này sẽ chứa các thư viện được đã được build hoàn chỉnh. Và có một số thứ yêu cầu phải cài như sau (làm theo hướng dẫn)

__Tesseract OCR__ ([tải ở đây](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe))
Hướng dẫn
Sau khi tải xong thì ấn vào cài đặt. Cái này thì không cần phải hướng dẫn nữa, chủ yêu là hướng dẫn cài ở đâu thôi. Giờ thì chọn thư mục cần cài, vào trong folder của dự án (`datatable-image-to-text`), vào tiếp `python/builds`, tạo một folder tên là `tesseract` rồi copy đường dẫn vào ô cài đặt.

<div align="center">
  <img src="https://github.com/NguyenAnhTuan1912/datatable-image-to-text/assets/86825061/5154656e-9261-4db1-b3f2-0071554b73cb" alt="Tesseract path guide"/>
</div>

Cuối cùng là ấn next và cài đặt. Sau khi cài xong thì kiếm một tấm hình có chữ, bỏ vào trong `python/test/images` rồi lấy tên file đó sửa trong `python/test/image_to_text.py` rồi thực thi script, kết quả sẽ được ghi ra file `python/test/out/regconized.txt`.

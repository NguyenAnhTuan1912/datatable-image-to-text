# Nhớ cài pytesseract với lệnh pip install pytesseract
# Cài luôn file tesseract: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe
# Thêm một số thư viện bắt buộc
import cv2
import pytesseract
import sys
import numpy as np

# Sử dụng sys để add utils vào mới có thể dùng module bên ngoài.
# sys.path.append('d:/Hoctap/Computer Vision/source')
sys.path.append('./')

from python.definitions import get_path

# KHAI BÁO BIẾN
# Khai báo một số đường dẫn mặc định trong thư mục test.
out_path = get_path("test/out")
images_path = get_path("test/images")
builds_path = get_path("builds")
# File out ở đây, nếu muốn tên file khác thì sửa ở dưới
outputtxt_path = get_path(out_path, "recognized.txt")
# Biến khác
used_lang = "vie"

# Gán đường dẫn tới file `tesseract.exe` vừa mới cài đặt ở bước trước vào đây.
pytesseract.pytesseract.tesseract_cmd = builds_path + "/tesseract/tesseract.exe"

# In một số thông tin
print("Languages that Tesseract OCR supports: ", pytesseract.get_languages())

# Đọc ảnh cần trích xuất chữ
img = cv2.imread(images_path + "/datatable04.png")

# Tiến hành giai đoạn 1: Tiền xử lý ảnh
# Chuyển ảnh màu thành ảnh xám (GRAY SCALE)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray image", gray)
cv2.waitKey(0)

# Tiến hành chuyển thành ảnh nhị phân
thresh, binary_img = cv2.threshold(gray, 128, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
inverted_binary_img = ~binary_img
# binary_img = ~cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Distinguish background and foreground", binary_img)
cv2.waitKey(0)

# Khởi tạo các thông số cho kernel
img_shape = np.array(binary_img).shape
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel_length = img_shape[1] // 80

# Tạo kernels để nhận diện chữ với shape (MORPH_RECT) và size ((18, 18))
# Với các kernel size khác nhau thì kết quả sẽ khác nhau
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
# Tạo lần lượt 2 kernels để erode cạnh ngang và cạnh dọc
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
# r_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (np.array(binary_img).shape[0] // 150, np.array(binary_img).shape[1] // 150))

print("Image shape: ", np.array(binary_img).shape)

# Erode ảnh để lấy lần lượt cạnh dọc và ngang
eroded_vertical_img = cv2.erode(binary_img, vertical_kernel, iterations = 5)
eroded_horizontal_img = cv2.erode(binary_img, horizontal_kernel, iterations = 5)

# Làm sáng và dày các cạnh với dilate
# dilation = cv2.dilate(binary_img, rect_kernel, iterations = 1)
vertical_lines = cv2.dilate(eroded_vertical_img, vertical_kernel, iterations = 5)
horizontal_lines = cv2.dilate(eroded_horizontal_img, horizontal_kernel, iterations = 5)

cv2.imshow("Vertical Lines", vertical_lines)
cv2.waitKey(0)

cv2.imshow("Horizontal Lines", horizontal_lines)
cv2.waitKey(0)

# Gộp ảnh chứa vertical và horizontal lines thành một. Lúc này thì mình có ảnh gồm các cạnh ngang và dọc.
alpha = 0.5
beta = 1.0 - alpha
vertical_horizontal_lines = cv2.addWeighted(vertical_lines, alpha, horizontal_lines, beta, 0.0)
vertical_horizontal_lines = cv2.erode(~vertical_horizontal_lines, kernel, iterations = 2)
thresh, vertical_horizontal_lines = cv2.threshold(vertical_horizontal_lines, 128, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

cv2.imshow("Lines", vertical_horizontal_lines)
cv2.waitKey(0)

# canny = cv2.Canny(gray, 100, 200)
# cv2.imshow("Canny", canny)
# cv2.waitKey(0)

# Tìm các contours
# Giai đoạn 2
contours, hierarchy = cv2.findContours(vertical_horizontal_lines, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sắp xếp các countours
# contours = sorted(contours, key=lambda x: cv2.contourArea(x))

# Tiến hành giai đoạn 3 và 4
# Tạo file txt nếu chưa có.
file = open(outputtxt_path, "w+")
file.write("")
file.close()

# Khai báo một biến để lưu kết quả.
text = ""
rect = None
iterationTimes = 0

# Tìm các bouding box
boundingBoxes = [cv2.boundingRect(contour) for contour in contours]

# Tìm height của mỗi bouding box
heights = [boundingBoxes[i][3] for i in range(len(boundingBoxes))]

# Tìm height của table
table_height = np.max(heights)

# Tính trung bình cộng của các height.
# mean_of_height = np.mean(heights)

print("Image's Area: ", img_shape[0] * img_shape[1])

# Với mỗi contour được xác định, thì mình sẽ lấy ra các bounding box tương ứng.
# Các tọa độ này sẽ được dùng để cắt ra các ảnh con chứa ảnh.
for boundingBox in boundingBoxes:
  # Tìm bounding box gồm tọa độ x, y, chiều rộng w và chiều cao h.
	x, y, w, h = boundingBox
 
	# Nếu như height của một box mà lớn hơn mean of height, thì loại box đó ra
	if h >= table_height: continue
	
	# Vẽ một hình chữ nhật màu xanh lá để cho trực quan (không ảnh hưởng)
	rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
	# Cắt ảnh
	cropped = inverted_binary_img[y:y + h, x:x + w]
	
	# Apply OCR on the cropped image
	predict = pytesseract.image_to_string(cropped, config='--psm 6', lang = used_lang)
	text += predict
	# print("Predict: ", predict)
	# cv2.imshow("Cropped", cropped)
	# cv2.waitKey(0)
	text += "\n"
 
cv2.imshow("Localization", rect)
cv2.waitKey(0)

# Mở file và ghi kết quả vào file txt.
file = open(outputtxt_path, "a", encoding="utf-8")
file.write(text)
file.close()
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

from python.definitions import get_path, TableType
from python.modules.imgpreprocessing import image_preprocess
from python.modules.characterslocalization import characters_localize

# KHAI BÁO BIẾN
# Khai báo một số đường dẫn mặc định trong thư mục test.
out_path = get_path("test/out")
images_path = get_path("test/images")
builds_path = get_path("builds")
# File out ở đây, nếu muốn tên file khác thì sửa ở dưới
outputtxt_path = get_path(out_path, "recognized.txt")
# Biến khác
used_lang = "vie"
table_type = TableType.ONLY_HORIZONTAL_LINES

# Gán đường dẫn tới file `tesseract.exe` vừa mới cài đặt ở bước trước vào đây.
pytesseract.pytesseract.tesseract_cmd = builds_path + "/tesseract/tesseract.exe"

# In một số thông tin
print("Languages that Tesseract OCR supports: ", pytesseract.get_languages())

# Đọc ảnh cần trích xuất chữ
img = cv2.imread(images_path + "/datatable07.jpg")

# Tiến hành giai đoạn 1: Tiền xử lý ảnh
binary_img, inverted_binary_img, img_shape = image_preprocess(img, table_type)

cv2.imshow("Lines", binary_img)
cv2.waitKey(0)

# Sắp xếp các countours
# contours = sorted(contours, key=lambda x: cv2.contourArea(x))

# Tiến hành giai đoạn 3 và 4
cnts, bboxes = characters_localize(binary_img, table_type)

# Tạo file txt nếu chưa có.
file = open(outputtxt_path, "w+")
file.write("")
file.close()

# Khai báo một biến để lưu kết quả.
text = ""
rect = None
iterationTimes = 0

# Tìm height của mỗi bouding box
heights = [bboxes[i][3] for i in range(len(bboxes))]

# Tìm height của table
table_height = np.max(heights)

# Tính trung bình cộng của các height.
# mean_of_height = np.mean(heights)

print("Image's Area: ", img_shape[0] * img_shape[1])

# Với mỗi contour được xác định, thì mình sẽ lấy ra các bounding box tương ứng.
# Các tọa độ này sẽ được dùng để cắt ra các ảnh con chứa ảnh.
for bbox in bboxes:
  # Tìm bounding box gồm tọa độ x, y, chiều rộng w và chiều cao h.
	x, y, w, h = bbox
 
	# Nếu như height của một box mà lớn hơn mean of height, thì loại box đó ra
	if h >= table_height: continue
	
	# Vẽ một hình chữ nhật màu xanh lá để cho trực quan (không ảnh hưởng)
	rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
	# Cắt ảnh
	cropped = inverted_binary_img[y:y + h, x:x + w]
	
	# Apply OCR on the cropped image
	# predict = pytesseract.image_to_string(cropped, config='--psm 6', lang = used_lang)
	# text += predict
	# print("Predict: ", predict)
	# cv2.imshow("Cropped", cropped)
	# cv2.waitKey(0)
	# text += "\n"
 
cv2.imshow("Localization", rect)
cv2.waitKey(0)

# Mở file và ghi kết quả vào file txt.
# file = open(outputtxt_path, "a", encoding="utf-8")
# file.write(text)
# file.close()
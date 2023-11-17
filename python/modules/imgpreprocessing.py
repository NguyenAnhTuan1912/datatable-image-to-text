import cv2
import numpy as np
import sys

# Sử dụng sys để add utils vào mới có thể dùng module bên ngoài.
# sys.path.append('d:/Hoctap/Computer Vision/source')
sys.path.append('./')

from python.definitions import TableType

def crop_image(img: cv2.UMat, x, y, w, h) -> cv2.UMat:
  """
  Hàm này dùng để cắt ảnh. Cho vào ảnh cần cắt, gốc tọa độ (x, y) của ảnh mới và chiều rộng, chiều
  cao mới của ảnh để cắt.

  Args:
      img (cv2.UMat): Ảnh cần cắt
      x (int): Điểm x của trong gốc tọa độ của ảnh mới.
      y (int): Điểm y của trong gốc tọa độ của ảnh mới.
      w (int): Chiều rộng tính từ điểm x của ảnh mới.
      h (int): Chiều cao tính từ điểm y của ảnh mới.

  Returns:
      cv2.UMat: Ảnh đã được cắt với các thông số được đưa vào.
  """
  return img[y:y + h, x:x + w]

def find_table_bboxes(binary_image: cv2.UMat, img_shape: tuple([int, int])):
  processed_binary_image = __n_table_image_preprocess(binary_image, img_shape)
  
  cv2.imshow("Processed Binary Image", processed_binary_image)
  cv2.waitKey(0)
  
  # Tìm contour của bảng
  cnts, cnts_hierarchy = cv2.findContours(processed_binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  # Khai báo một số biến.
  table_bbox = None
  bboxes = []
  heights = []
  index = -1
  max = 0
  
  for cnt in cnts:
    bbox = cv2.boundingRect(cnt)
    x, w, y, h = bbox
    
    if h > max:
      max = h
      index = index + 1
    
    heights.append(h)
    bboxes.append(bbox)
    
  heights.pop(index)
  table_bbox = bboxes.pop(index)
  
  return table_bbox, bboxes, heights

def convert_to_binary(img: cv2.UMat) -> tuple([cv2.UMat, cv2.UMat, tuple([int, int])]):
  """
  Hàm này dùng để chuyển ảnh thành ảnh nhị phân với OTSU. Ngoài ra hàm còn trả về hình ảnh nghịch đảo bit
  của ảnh nhị phân cùng với kích thước của ảnh.

  Args:
      img (cv2.UMat): Ảnh cần chuyển thành nhị phân.

  Returns:
      tuple([cv2.UMat, cv2.UMat, tuple([int, int])]): Ảnh nhị phân và nghịch đảo bit của ảnh nhị phân.
  """
  # Chuyển ảnh màu thành ảnh xám (GRAY SCALE)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  # Chuyển ảnh màu thành ảnh xám (GRAY SCALE)
  result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  # Tiến hành chuyển thành ảnh nhị phân
  thresh, result = cv2.threshold(gray, 128, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
  inverted_binary_img = ~result
  
  return result, inverted_binary_img, np.array(result).shape

def __n_table_image_preprocess(
  binary_img: cv2.UMat,
  img_shape: tuple([int, int]),
  kl_division: int = 80,
  ksize: tuple([int, int]) = (3, 3)
) -> cv2.UMat:
  """
  Hàm này dùng để xử lý ảnh có chứa kiểu bảng bình thường (Normal table).

  Args:
    binary_img (cv2.UMat): Ảnh nhị phân cần được xử lý.
    img_shape (tuple(int, int)): Kích thước của ảnh.
    kl_division (int): Số chia dùng trong phép tính kernel length.
    ksize (tuple(int, int)): Kích thước của kernel dùng để erode kết quả.

  Returns:
    cv2.UMat: Ảnh nhị phân đã qua xử lý. Là ảnh mà các đường viền trong bảng được làm dày.
  """
  # Khai báo một số biến.
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize)
  kernel_length = img_shape[1] // kl_division
  
  # Tạo lần lượt 2 kernels để erode và dilate cạnh ngang và cạnh dọc
  vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
  horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
  
  # Erode ảnh để lấy lần lượt cạnh dọc và ngang
  eroded_vertical_img = cv2.erode(binary_img, vertical_kernel, iterations = 5)
  eroded_horizontal_img = cv2.erode(binary_img, horizontal_kernel, iterations = 5)

  # Làm sáng và dày các cạnh với dilate
  vertical_lines = cv2.dilate(eroded_vertical_img, vertical_kernel, iterations = 5)
  horizontal_lines = cv2.dilate(eroded_horizontal_img, horizontal_kernel, iterations = 5)
  
  alpha = 0.5
  beta = 1.0 - alpha
  result = cv2.addWeighted(vertical_lines, alpha, horizontal_lines, beta, 0.0)
  result = cv2.erode(~result, kernel, iterations = 2)
  thresh, result = cv2.threshold(result, 128, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
  
  return  result

def __ohl_table_image_preprocess(binary_img, img_shape) -> cv2.UMat:
  """
  Hàm này sẽ xử lý ảnh mà bảng của nó chỉ có các đường viền ngang (Only horizontal lines table).

  Args:
      binary_img (cv2.UMat): Ảnh nhị phân cần được xử lý.
      img_shape (cv2.UMat): Kích thước của ảnh.

  Returns:
      cv2.UMat: Ảnh nhị phân đã được xử lý.
  """
  # Copy ảnh
  copy = binary_img.copy()
  
  # Khai báo một số biến.
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
  kernel_length = img_shape[1] // 80
  
  # Lấy kernel để erode và dilate đường viền ngang.
  horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
  
  eroded_horizontal_img = cv2.erode(binary_img, horizontal_kernel, iterations = 5)
  result = cv2.dilate(eroded_horizontal_img, horizontal_kernel, iterations = 5)
  
  # Xóa các đường viền ngang.
  # Tìm contours của các đường này trước.
  cnts, cnts_hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  cv2.drawContours(copy, cnts, -1, (0, 0, 0), 3)
  
  cv2.imshow("Remove horizontal line", copy)
  cv2.waitKey(0)
  
  # Dilate chữ
  result = cv2.dilate(copy, kernel, iterations = 1)
  
  return result

def __ovl_table_image_preprocess(binary_img, img_shape) -> cv2.UMat:
  """
  Hàm này sẽ xử lý ảnh mà bảng của nó chỉ có các đường viền dọc (Only vertical lines table).

  Args:
      binary_img (cv2.UMat): Ảnh nhị phân cần được xử lý.
      img_shape (cv2.UMat): Kích thước của ảnh.

  Returns:
      cv2.UMat: Ảnh nhị phân đã được xử lý.
  """
  # Copy ảnh
  copy = binary_img.copy()
  
  # Khai báo một số biến.
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))
  kernel_length = img_shape[1] // 80
  
  # Lấy kernel để erode và dilate đường viền ngang.
  vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
  
  eroded_vertical_img = cv2.erode(binary_img, vertical_kernel, iterations = 5)
  result = cv2.dilate(eroded_vertical_img, vertical_kernel, iterations = 5)
  
  # Xóa các đường viền dọc.
  # Tìm contours của các đường này trước.
  cnts, cnts_hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  cv2.drawContours(copy, cnts, -1, (0, 0, 0), 3)
  
  cv2.imshow("Remove horizontal line", copy)
  cv2.waitKey(0)
  
  # Dilate chữ
  result = cv2.dilate(copy, kernel, iterations = 1)
  
  return

def __ocb_table_image_preprocess(binary_img, img_shape) -> cv2.UMat:
  """
  Hàm này sẽ xử lý ảnh mà bảng của nó chỉ có các đường viền bao quanh (Only borders table).

  Args:
      binary_img (cv2.UMat): Ảnh nhị phân cần được xử lý.
      img_shape (cv2.UMat): Kích thước của ảnh.

  Returns:
      cv2.UMat: Ảnh nhị phân đã được xử lý.
  """
  # Khai báo một số biến.
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))
  
  result = __n_table_image_preprocess(binary_img, img_shape)
  
  copy = binary_img.copy()
  
  cv2.imshow("RESULT", result)
  cv2.waitKey(0)
  
  # Xóa các đường viền dọc và ngang.
  # Tìm contours của các đường này trước.
  cnts, cnts_hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  cv2.drawContours(copy, cnts, -1, (0, 0, 0), 10)
  
  cv2.imshow("Remove horizontal line", copy)
  cv2.waitKey(0)
  
  # Dilate chữ
  result = cv2.dilate(copy, kernel, iterations = 1)
  
  return result

def __nb_table_image_preprocess(binary_img, img_shape):
  return

def image_preprocess(img, type: TableType = TableType.NORMAL) -> tuple([cv2.UMat, cv2.UMat, tuple([int, int])]):
  """
  Hàm này sẽ chịu trách nhiệm cho việc xử lý ảnh (Image Preprocessing Stage). Trả về ảnh nhị phân đã được xử lý.

  Args:
    img (UMat): Ảnh gốc cần được xử lý.
    type (TableType): Kiểu của table.

  Returns:
    tuple([cv2.UMat, cv2.UMat, tuple([int, int])]):
      - Ảnh nhị phân đã được xử lý.
      - Ảnh nhị phân đã được nghịch đảo (chưa qua xử lý).
      - Kích thước ảnh (w, h).
  """
  # Tiến hành giai đoạn 1: Tiền xử lý ảnh
  # Chuyển thành ảnh nhị phân
  binary_img, inverted_binary_img, img_shape = convert_to_binary(gray)
  
  if type == TableType.NORMAL:
    return __n_table_image_preprocess(binary_img, img_shape), inverted_binary_img, img_shape
  
  if type == TableType.ONLY_HORIZONTAL_LINES:
    return __ohl_table_image_preprocess(binary_img, img_shape), inverted_binary_img, img_shape
  
  if type == TableType.ONLY_VERTICAL_LINES:
    return __ovl_table_image_preprocess(binary_img, img_shape), inverted_binary_img, img_shape

  if type == TableType.ONLY_COVERED_BORDERS: 
    return __ocb_table_image_preprocess(binary_img, img_shape), inverted_binary_img, img_shape
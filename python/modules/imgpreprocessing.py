import cv2
import numpy as np
import sys

# Sử dụng sys để add utils vào mới có thể dùng module bên ngoài.
# sys.path.append('d:/Hoctap/Computer Vision/source')
sys.path.append('./')

from python.definitions import TableType

def __n_table_image_preprocess(binary_img, img_shape) -> cv2.UMat:
  """
  Hàm này dùng để xử lý ảnh có chứa kiểu bảng bình thường (Normal table).

  Args:
    binary_img (UMat): Ảnh nhị phân đã được xử lý trước đó.
    img_shape (Tuple(int, int)): Kích thước của ảnh.

  Trả về:
    UMat: Ảnh nhị phân đã qua xử lý. Là ảnh mà các đường viền trong bảng được làm dày.
  """
  # Khai báo một số biến.
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
  kernel_length = img_shape[1] // 80
  
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
  result = cv2.addWeighted(vertical_lines, alpha, horizontal_lines, beta, 1)
  result = cv2.erode(~result, kernel, iterations = 2)
  thresh, result = cv2.threshold(result, 128, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
  return  result

def __ohl_table_image_preprocess(binary_img, img_shape):
  # Copy ảnh
  copy = binary_img.copy()
  
  # Khai báo một số biến.
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))
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

def __ovl_table_image_preprocess(binary_img, img_shape):
  return

def __ocb_table_image_preprocess(binary_img, img_shape):
  return

def __nb_table_image_preprocess(binary_img, img_shape):
  return

def image_preprocess(img, type: TableType = TableType.NORMAL_TABLE) -> tuple([cv2.UMat, cv2.UMat, tuple([int, int])]):
  """
  Hàm này sẽ chịu trách nhiệm cho việc xử lý ảnh.
  (Image Preprocessing Stage)

  Tham số:
    img (UMat): Ảnh gốc cần được xử lý.
    type (TableType): Kiểu của table.

  Trả về:
    tuple([cv2.UMat, cv2.UMat, tuple([int, int])]):
      - Ảnh nhị phân đã được xử lý.
      - Ảnh nhị phân đã được nghịch đảo (chưa qua xử lý).
      - Kích thước ảnh (w, h).
  """
  # Tiến hành giai đoạn 1: Tiền xử lý ảnh
  # Chuyển ảnh màu thành ảnh xám (GRAY SCALE)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  # Tiến hành chuyển thành ảnh nhị phân
  thresh, binary_img = cv2.threshold(gray, 128, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
  inverted_binary_img = ~binary_img
  img_shape = np.array(binary_img).shape
  
  if type == TableType.NORMAL_TABLE:
    return __n_table_image_preprocess(binary_img, img_shape), inverted_binary_img, img_shape
  
  if type == TableType.ONLY_HORIZONTAL_LINES:
    return __ohl_table_image_preprocess(binary_img, img_shape), inverted_binary_img, img_shape
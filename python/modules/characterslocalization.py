import cv2
import sys

# Sử dụng sys để add utils vào mới có thể dùng module bên ngoài.
# sys.path.append('d:/Hoctap/Computer Vision/source')
sys.path.append('./')

from python.definitions import TableType

def characters_localize(binary_img, type: TableType = TableType.NORMAL_TABLE) -> tuple([[cv2.UMat], [cv2.typing.Rect]]):
  """
  Hàm này sẽ định vị trí của các từ trong bảng.

  Tham số:
    binary_img (UMat): Ảnh nhị phân đã qua giai đoạn Image Preprocessing.
    type (TableType): Kiểu của table.

  Trả về:
    tuple([[cv2.UMat], [cv2.typing.Rect]]): Các contours.
  """
  cnts, cnts_hierarchy = [1, 2]
  bboxes = []
  if type == TableType.NORMAL_TABLE:
    cnts, cnts_hierarchy = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    bboxes = [cv2.boundingRect(ccnt) for ccnt in cnts]
    
  if type == TableType.ONLY_HORIZONTAL_LINES:
    cnts, cnts_hierarchy = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    bboxes = [cv2.boundingRect(ccnt) for ccnt in cnts]
    
  return cnts, bboxes
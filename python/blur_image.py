import cv2
import sys

# Sử dụng sys để add utils vào mới có thể dùng module bên ngoài.
# sys.path.append('d:/Hoctap/Computer Vision/source')
sys.path.append('./')

from utils.myimage import MyImage

# Tạo instance của MyImage
mi = MyImage()

# Lấy các tham số cần thiết
img = sys.argv[0]
strength = sys.argv[1]

# Tiến hành làm mờ ảnh

sys.stdout.flush()
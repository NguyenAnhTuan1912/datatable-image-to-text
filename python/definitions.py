# Khai báo và định nghĩa một số biến toàn cục
import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(*paths):
  """
  Dùng hàm này để lấy ra đường dẫn tuyệt đối tới một file bất kì.
  """
  
  return os.path.normpath(os.path.join(ROOT_DIR, *paths))
from lib.download import download
import cv2
import numpy as np

source = 'https://opencv-python-tutroals.readthedocs.io/en/latest/_static/opencv-logo-white.png'

binaryData = download(source)
arr = np.fromstring(binaryData, dtype=np.uint8)
img = cv2.imdecode(arr, 1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

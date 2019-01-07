import cv2
import numpy as np

img = cv2.imread('De1.jpg', 0)

rows,cols = img.shape
print img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1)
img = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
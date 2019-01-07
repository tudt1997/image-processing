import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

i = cv2.imread('De1.jpg')

rows, cols, channels = i.shape

s = i
s[:, 0, :] = i[:, 0, :]

for c in range(1, cols):
    s[:, c, :] = 2 * i[:, c, :] - i[:, c - 1, :]

test = s[:,:,2]
unique, counts = np.unique(test, return_counts=True)
print test.shape
print unique[counts.argmax()]
print counts.max()

cv2.imshow('Image', s)
cv2.waitKey(0)
cv2.destroyAllWindows()

histr = cv2.calcHist([s], [2], None, [256], [0,256])
plt.plot(histr)
plt.show()
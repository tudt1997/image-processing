import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy import signal

# img = cv2.imread('')

# rows, cols, channels = img.shape

f = open('matrix.txt', 'r')

rowA, columnA = f.readline().split(' ')
rowA, columnA = int(rowA), int(columnA)
matrixA = np.zeros((rowA, columnA), dtype=np.float32)

for i in range(rowA):
    matrixA[i] = np.asarray(f.readline().split(' '))
print(matrixA)

rowB, columnB = f.readline().split(' ')
rowB, columnB = int(rowB), int(columnB)
matrixB = np.zeros((rowB, columnB), dtype=np.float32)

for i in range(rowB):
    matrixB[i] = np.asarray(f.readline().split(' '))
matrixB = matrixB / matrixB.sum()
print(matrixB)

# out = signal.convolve2d(matrixA, matrixB, mode='same')

# out = np.divide(out, np.sum(matrixB))
out = cv2.filter2D(matrixA, -1, matrixB)
print(out)

# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

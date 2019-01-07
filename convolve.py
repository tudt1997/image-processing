from scipy import signal
import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
f = open('matrix.txt', 'r')
rowA, columnA = f.readline().split(' ')
rowA, columnA = int(rowA), int(columnA)
matrixA = np.zeros((rowA, columnA), dtype=np.float32)
for i in range(rowA):
    matrixA[i] = np.asarray(f.readline().split(' '))
print("I2 = ")
print(matrixA)
maxA = np.max(matrixA)
matrixA = np.divide(matrixA, maxA)
print("I3 = ")
print(matrixA)
rowB, columnB = f.readline().split(' ')
rowB, columnB = int(rowB), int(columnB)
matrixB = np.zeros((rowB, columnB), dtype=np.float32)
for i in range(rowB):
    matrixB[i] = np.asarray(f.readline().split(' '))
print(matrixB)

out = signal.convolve2d(matrixA, matrixB, mode='full')
print("Sum = " + str(np.sum(matrixB)))
print("I4 = ")
out = np.divide(out, np.sum(matrixB))
print(out)

print("Max = " + str(maxA))
out = np.multiply(out, maxA)
print("I5 = ")
print(np.round(out))
f.close()
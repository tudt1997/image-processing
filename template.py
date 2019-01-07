import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

img = cv2.imread('', 0)

rows, cols, channels = img.shape



cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
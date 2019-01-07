import numpy as np, cv2

def convolve(image, kernel, stride=1):
    (iH, iW, iC) = image.shape
    (kH, kW) = kernel.shape[:2]

    # calculate padding size
    pad_x = (stride * iW - stride - iW + kW) / 2.
    if pad_x%2!=0:
        pad_left = int(pad_x - 0.5)
        pad_right = int(pad_x + 0.5)
    else:
        pad_left=pad_right=int(pad_x)

    pad_y = (stride * iH - stride - iH + kH) / 2.
    if pad_y%2!=0:
        pad_top = int(pad_y - 0.5)
        pad_bottom = int(pad_y + 0.5)
    else:
        pad_top= pad_bottom= int(pad_y)

    #pad image
    image = cv2.copyMakeBorder(image, pad_top, pad_bottom, pad_left, pad_right, 0)

    #initialise output image
    output= np.zeros((iH, iW, iC), dtype=np.float32)

    #convolve
    for y in range(pad_top, iH + pad_top):
        for x in range(pad_left, iW + pad_left):
            roi = image[y - pad_top: y + pad_bottom + 1, x - pad_left: x + pad_right + 1]
            k = (roi.transpose(2,0,1) * kernel).sum(2).sum(1)
            output[y - pad_top, x - pad_left] = k
    return output

G = np.array(cv2.imread('De1.jpg'), dtype=np.float32)
M = np.ones([4, 4]) / 16.
J = convolve(G, M)

print 'G shape', G.shape
print 'J shape', J.shape

cv2.imshow('J', J/255.)
cv2.waitKey(0)

K= G-J
U= 0.5*K + J

cv2.imshow('U', U/255.)
cv2.waitKey(0)
# 0603.py
import cv2
import numpy as np

src = cv2.imread('../data/rect.jpg', cv2.IMREAD_GRAYSCALE)
#1
gx = cv2.Sobel(src, cv2.CV_32F, 1, 0, ksize = 3) #수평마스크, 수직엣지
gy = cv2.Sobel(src, cv2.CV_32F, 0, 1, ksize = 3) #수직마스크, 수평엣지

#2
dstX = cv2.sqrt(np.abs(gx)) #절대값, 루트
#차이에 대해 0~255 정규
dstX = cv2.normalize(dstX, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

#3
dstY = cv2.sqrt(np.abs(gy))
dstY = cv2.normalize(dstY, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

#4
#루트 ((gx)^2+(gy)^2)
mag   = cv2.magnitude(gx, gy)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(mag)
print('mag:', minVal, maxVal, minLoc, maxLoc)

dstM = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

cv2.imshow('src',  src)
cv2.imshow('dstX',  dstX)    
cv2.imshow('dstY',  dstY)
cv2.imshow('dstM',  dstM)

cv2.waitKey()
cv2.destroyAllWindows()

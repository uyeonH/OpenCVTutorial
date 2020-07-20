import cv2
import numpy as np
src = cv2.imread('../data/srcThreshold.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src',  src)

ret, dst = cv2.threshold(src, 0, 255,
                             cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('dst',  dst)
print('ret=',ret)
#adaptiveThreshold(src, max_val, adaptiveMethod,thresholdType, blockSize, C[, dst])
#51=blocksize, 7=보정값
dst2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, 41, 7)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C',  dst2)

dst3 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 41, 7)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C',  dst3)

cv2.waitKey()    
cv2.destroyAllWindows()

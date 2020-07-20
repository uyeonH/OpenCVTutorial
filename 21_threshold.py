# 0501.py
import cv2
import numpy as np
src = cv2.imread('./data/heart10.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src',  src)
#(이미지파일, 임계값,임계값을 넘었을 때 적용할 value, type)
#cv2.THRESH_BINARY_INV는 픽셀 값이 임계값보다 크면 임계값. 작으면 그대로 할당
ret, dst = cv2.threshold(src, 200, 255, cv2.THRESH_BINARY_INV) 
print('ret=', ret)
cv2.imshow('dst',  dst)
#+는 두 타입 모두 적용
#cv2.THRESH_BINARY는 픽셀값이 임계값보다 크면 value, 작으면 0으로 할당
#cv2.THRESH_OTSU는 임계값 상관 없이 최적의 값으로 

ret2, dst2 = cv2.threshold(src, 200, 255,
                             cv2.THRESH_BINARY+cv2.THRESH_OTSU)

print('ret2=', ret2)
cv2.imshow('dst2',  dst2)

cv2.waitKey()    
cv2.destroyAllWindows()

# 0602.py
import cv2
import numpy as np

src = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)

#medianFilter 중간값필터 잇는 색상으로
dst1= cv2.medianBlur(src, ksize = 7)

#mean 평균값
dst2 = cv2.blur(src, ksize=(7, 7))

#gaussianFilter
dst3 = cv2.GaussianBlur(src, ksize=(7, 7), sigmaX=0.0)
dst4 = cv2.GaussianBlur(src, ksize=(7, 7), sigmaX=10.0)

#직접 만들기
#kernel = np.ones((3,3),np.float32)/9.0 => 같은 의미
kernel=np.array([[1.0/9.0,1.0/9.0,1.0/9.0],
                 [1.0/9.0,1.0/9.0,1.0/9.0],
                 [1.0/9.0,1.0/9.0,1.0/9.0]])

dst=cv2.filter2D(src,-1,kernel)

cv2.imshow('dst',  dst) 
cv2.imshow('dst1',  dst1)    
cv2.imshow('dst2',  dst2)
cv2.imshow('dst3',  dst3)
cv2.imshow('dst4',  dst4)

cv2.waitKey()    
cv2.destroyAllWindows()

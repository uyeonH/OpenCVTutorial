# 0809.py
import cv2
import numpy as np

#1
src =cv2.imread('../data/momentTest.jpg')
cv2.imshow('src_ori',  src)
src=cv2.rotate(src,cv2.ROTATE_90_CLOCKWISE)
#src=cv2.resize(src,dsize=(0,0),fx=1.2,fy=1.2)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, bImage = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
cv2.imshow('src',  src)
#2
##M = cv2.moments(bImage)   
M = cv2.moments(bImage, True)
for key, value in M.items():
    print('{}={}'.format(key, value))

    #m00=79262
    
#3
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
dst = src.copy()

cv2.circle(dst, (cx, cy), 5, (0,0,255), 2)
hu = cv2.HuMoments(M)
print(hu)

cv2.imshow('dst',  dst)
cv2.waitKey()
cv2.destroyAllWindows()

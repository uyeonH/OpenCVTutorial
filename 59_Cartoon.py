import cv2
import numpy as np

cap=cv2.VideoCapture('./data/dog.mp4')

while True:
    
    ret,img=cap.read()
    img=cv2.resize(img,None,fx=0.2,fy=0.2)
    if ret:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #gray color
        img_gray = cv2.medianBlur(img_gray, 7) #remove noise

        edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
        ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV) #binary_inv 흰 바탕에 검은 선

        sketch=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
        sigma_color = 5
        sigma_space = 7
        size = 5
        for i in range(15):
            img_bi=cv2.bilateralFilter(img,size,sigma_color,sigma_space)
        dst=cv2.bitwise_and(img_bi,img_bi,mask=mask)
        key = cv2.waitKey(25)
        if key == 27: # Esc
           break
        #cv2.imshow('sketch',sketch)
        #cv2.imshow('sketch',img_bi)
        cv2.imshow('ori',img)
        cv2.imshow('dst',dst)
        cv2.waitKey(20)
        
    else:
        break
cap.release()
cv2.waitKey()
cv2.destroyAllWindows()

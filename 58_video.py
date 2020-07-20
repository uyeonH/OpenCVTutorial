import cv2
import numpy as np

cap = cv2.VideoCapture('../data/vtest.avi') 
flag=True

while True:
    retval, frame = cap.read() 
    if not retval:
        break
    cv2.imshow('frame',frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    if bool(flag):
        roi = cv2.selectROI('img',frame)
        roi_h = h[roi[1]:roi[1]+roi[3],roi[0]+roi[2]]
        flag=False
    else:    
        hist = cv2.calcHist([roi_h], [0], None,[64], [0, 256]) 
        backP= cv2.calcBackProject([h.astype(np.float32)], [0], hist,[0, 256],scale=1.0)
        hist = cv2.sort(hist, cv2.SORT_EVERY_COLUMN+cv2.SORT_DESCENDING)
        k = 1 
        T = hist[k][0] -1 
        ret, dst = cv2.threshold(backP, T, 255, cv2.THRESH_BINARY)
        cv2.imshow('frame',dst)
        
    key = cv2.waitKey(25)
    if key == 27: # Esc
       break
    
if cap.isOpened():
    cap.release()
cv2.imshow('frame',frame)    
#cv2.waitKey()    
cv2.destroyAllWindows()

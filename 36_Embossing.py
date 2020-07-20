# 0701.py
import cv2
import numpy as np

src = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)

#edges1 = cv2.Canny(src, 50, 100)
#edges2 = cv2.Canny(src, 50, 200)
 
#cv2.imshow('edges1',  edges1)
#cv2.imshow('edges2',  edges2)

kernel=np.array([[0,-1,-1],[1,0,-1],[1,1,0]])

kernel=np.array([[-1,-1,0],[-1,0,1],[0,1,1]])

dst=cv2.filter2D(src,-1,kernel)

dst=cv2.imshow('Embossing',dst)

cv2.waitKey()
cv2.destroyAllWindows()

import cv2
import numpy as np

src = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)

#cv2.imshow('src',  src)

size=15
kernel=np.zeros((size,size))
kernel[int((size-1)/2),: ]=np.ones(size) #수평 흔들림
#kernel[:,int((size-1)/2) ]=np.ones(size) #수직 흔들림

kernel=kernel/size

dst=cv2.filter2D(src,-1,kernel)
cv2.imshow('src',  dst)

cv2.waitKey()
cv2.destroyAllWindows()
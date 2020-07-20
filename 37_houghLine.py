import cv2
import numpy as np

src = cv2.imread('../data/rect.jpg')
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 100)
#rho=1 픽셀 1단위로, 180도
lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180.0, threshold=100)

print('lines.shape=', lines.shape) #(4,1,2) 2는 로와 세타 쌍
print('lines=', lines)

for line in lines:
    rho, theta   = line[0]
    c = np.cos(theta)
    s = np.sin(theta)
    
    #양 끝점을 찾아내야한다, 호프는 로랑 세타만 알려줌
    #x0, y0는 원점에서 직선에 수직을 내린 지점
    x0 = c*rho
    y0 = s*rho

    x1 = int(x0 + 1000*(-s))
    y1 = int(y0 + 1000*(c))
    
    x2 = int(x0 - 1000*(-s))
    y2 = int(y0 - 1000*(c))
    
    cv2.line(src, (x1,y1), (x2,y2), (0,255,255), 2)
    
cv2.imshow('edges',  edges)
cv2.imshow('src',  src)
cv2.waitKey()
cv2.destroyAllWindows()

import cv2 # OpenCV 라이브러리 import
from matplotlib import pyplot as plt # matplotlib.pyplot 라이브러리 import

imageFile = '../data/lena.jpg' # 영상 파일 이름

imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(3,3))
plt.subplots_adjust(left=0.3, right=0.9, bottom=0, top=1)
plt.imshow(imgGray, cmap = 'gray')

##plt.axis('tight')
plt.axis('off')
plt.savefig('../data/0205.png')
plt.show()

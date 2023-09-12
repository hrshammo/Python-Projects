import cv2
import numpy as np
img = cv2.imread('images.jpg',1)
new_img=cv2.resize(img,(img.shape[1]//2,img.shape[0]//3))
cv2.imshow('new_img',new_img)
cv2.waitKey(0)
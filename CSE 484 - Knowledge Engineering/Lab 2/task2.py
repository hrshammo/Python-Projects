import cv2
import numpy as np
img = cv2.imread('images.jpg',1)
new_img= img[50:100, 50:100]
cv2.imshow('new_img',new_img)
cv2.imshow('img',img)
cv2.imwrite("img.jpeg", new_img)
cv2.waitKey(0)
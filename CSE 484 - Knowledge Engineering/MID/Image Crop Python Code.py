import cv2
import numpy as np
img=cv2.imread('flower.jpg',1)
#new_img=cv2.resize(img,(img.shape[1]//2,img.shape[0]//3))

#cv2.imshow('new_img',new_img)

new_img=img[50:100,50:100]
cv2.imshow('new_img',new_img)
cv2.imshow('img',img)

cv2.waitKey(0)


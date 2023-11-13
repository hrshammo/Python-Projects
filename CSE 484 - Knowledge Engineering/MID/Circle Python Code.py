import cv2
import numpy as np
img=cv2.imread('flower.jpg',1)
#new_img=cv2.resize(img,(img.shape[1]//2,img.shape[0]//3))

#cv2.imshow('new_img',new_img)

#new_img=img[50:100,50:100]
#cv2.imshow('new_img',new_img)
#cv2.imshow('img',img)
#img_draw=cv2.rectangle(img, pt1=(50,50), pt2=(100,300), color=(0,0,0), thickness=3)
img_draw2=cv2.circle(img, center=(50,50), radius= 30, color=(0,0,0), thickness=3)
cv2.imshow('Image',img_draw2)
cv2.waitKey(0)




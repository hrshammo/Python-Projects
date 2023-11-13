import cv2
import numpy as np
img=cv2.imread('flower.jpg',1)
new_img=cv2.resize(img,(img.shape[1]//2,img.shape[0]//3))
def draw(event,x,y,flags,params):
   if event==1:
       cv2.circle(new_img,center=(x,y),radius=50,color=(0,0,255),thickness=3)

cv2.namedWindow(winname="abc")
cv2.setMouseCallback("abc",draw)

while True:
   cv2.imshow('abc', new_img)

   if cv2.waitKey(1) & 0xFF== ord('x'):
       break


cv2.destroyAllWindows()




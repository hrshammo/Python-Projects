import cv2
import numpy as np
img=cv2.imread('flower.jpg',1)
new_img=cv2.resize(img,(img.shape[1]//2,img.shape[0]//3))
flag=False
ix=-1
iy=-1
def draw(event,x,y,flags,params):
   global flag,ix,iy
   if event==1:
       flag=True
       ix=x
       iy=y
   elif event==4:
       flag=False
       cv2.rectangle(new_img, pt1=(ix, iy), pt2=(x, y), color=(0, 0, 255), thickness=3)
       crop_img=new_img[iy:y,ix:x]
       cv2.imshow("croped",crop_img)
       cv2.waitKey(0)

cv2.namedWindow(winname="abc")
cv2.setMouseCallback("abc",draw)

while True:
   cv2.imshow('abc', new_img)

   if cv2.waitKey(1) & 0xFF== ord('x'):
       break


cv2.destroyAllWindows()




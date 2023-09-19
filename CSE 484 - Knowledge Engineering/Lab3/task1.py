import cv2
import numpy as np
#img=cv2.imread('sunset-1373171_1920.jpg',1)
img=cv2.imread('a.webp',1)
flag=False
ix=-1
iy=-1

#new_img=cv2.resize(img(img.shape[1]//5,img.shape[0]//5))

def draw(event,x,y,flags,params):
    global flag,ix,iy
    if event==1:
        #cv2.circle(img,center=(x,y),radius=50,color=(0,0,0),thickness=3)
        #cv2.rectangle(img, pt1=(x,y), pt2=(x+10,y+34), color=(0,0,0),thickness=2)
        flag=True
        ix=x
        iy=y
    if event==0
        cv2.rectangle(img,pt1=(ix,iy), pt2=(x+10,y+34), color=(0,0,0),thickness=2)
cv2.namedWindow(winname="Window")
cv2.setMouseCallback("Window",draw)
while True:
    cv2.imshow("Window", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break


cv2.destroyAllWindows()

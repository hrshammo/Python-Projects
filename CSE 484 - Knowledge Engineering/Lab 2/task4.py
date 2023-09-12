import cv2
import numpy as np
img = cv2.imread('images.jpeg',1)
def draw(event,x,y,flags,params):
    print("BangBang")
cv2.namedWindow(winname="Window")
cv2.setMouseCallback("window",draw)
while True:
    cv2.imshow("img",img)
    if cv2.waitKey(1) & 0xFF== ord('x'):
        break

cv2.destroyAllWindows()
import cv2
import numpy as np
img = cv2.imread('images.jpg',1)
img_draw = cv2.rectangle(img, pt1=(53,10), pt2=(133,60), color=(0,0,0),thickness=2)
img_draw = cv2.circle(img,center=(190,30), radius=30,color=(0,0,0),thickness=2)
img_draw = cv2.line(img,pt1=(135,37),pt2=(160,30) ,color=(0,0,0),thickness=2)
img_draw = cv2.putText(img,org=(200,140),fontScale=0.51, fontFace=cv2.FONT_ITALIC,color=(0,0,0),thickness=2,lineType=cv2.LINE_AA, text="BANG BANG")
cv2.imshow("draw",img_draw)
cv2.waitKey(0)
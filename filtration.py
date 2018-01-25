import numpy as np
import cv2 as cv
import image as img
import math
img=cv.imread("coins4.jpeg")
height,width,channel=img.shape


#filtering

#Median filtering

a=0
b=0
for d in range(5):
	for h in range(3,height,+3):
		for w in range(3,width,+3):
			q=[]
			for i in range(a,h):
				for j in range(b,w):
					q.append(np.average(img[i][j]))
			avg=np.median(q)
			for i in range(a,h):
				for j in range(b,w):
					img[i,j]=avg
			b=w
		a=h			
cv.imshow("Test image",img)
cv.waitKey(2000)

#spatial averaging

h=height-1
w=width-1
for d in range(5):
	for i in range(0,h):
		for j in range(0,w):
			a=np.average(img[i,j])
			b=np.average(img[i+1,j])
			c=np.average(img[i,j+1])
			avg=(1/2)*(a+((1/2)*(b+c)))
			img[i,j]=avg
cv.imshow("Test image",img)
cv.waitKey(0)
				
				
				

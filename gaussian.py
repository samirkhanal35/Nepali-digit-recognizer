import numpy as np
import cv2 as cv
import grayconversion
import filtration

img = cv.imread('sample.png')

img = grayconversion.conversion(img)
img=filtration.filtration(img)

img1=img.copy()
#cv.imshow("",img)
#cv.waitKey(2000)
height = img.shape[0]
width = img.shape[1]

gauss = (1.0/57)*np.array(
[[0,1,2,1,0],
[1,3,5,3,1],
[2,5,9,5,2],
[1,3,5,3,1],
[0,1,2,1,0]])


for rep in range(0,1):
	#sum(sum(gauss))

	for i in np.arange(2, height-2):
		for j in np.arange(2, width-2):
			sum = 0
			for k in np.arange(-2 ,3):
				for l in np.arange(-2 ,3):
					a = img[i+k, j+l]
					p = gauss[2+k, 2+l]
					sum = sum + (p*a)
			b = sum
			img1[i,j]=b		
			
#cv.imwrite('filter.png',img1)
cv.imshow('gaussian',img1)
img=img1.copy()
cv.waitKey(2000)

#binarization
for i in range(0,height):
		for j in range(0,width):
			if np.average(img[i,j])>=100 :
				img[i,j]=255
			else :
				img[i,j]=0	
cv.imshow("binarized",img)
cv.waitKey(0)



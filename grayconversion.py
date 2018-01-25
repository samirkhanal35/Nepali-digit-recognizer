def conversion(img):
	import cv2
	#img=cv2.imread("coins.jpg")
	cv2.imshow("demo",img)
	cv2.waitKey(2000)
	heighty,widthx,channel=img.shape
	print (widthx,heighty,channel)
	for i in range(0,heighty):
		for j in range(0,widthx):
			red=img[i,j,0]
			blue=img[i,j,1]
			green=img[i,j,2]
			avg=(0.21*red)+(0.72*blue)+(0.07*green)
			img[i,j]=avg
	cv2.imshow("demo",img)
	cv2.waitKey(0)
	

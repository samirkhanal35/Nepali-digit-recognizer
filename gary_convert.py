def gray_con(num1,num2,img):
    import math
    import cv2
#*******GRAYSCALE_CONVERSION_LIGHTNESS_METH*******
    for i in range(0,num1):
        for j in range(0,num2):
            red=img[i,j,2]              #read RED_COLOR value of current pixel
            green=img[i,j,1]            #read GREEN_COLOR value of current pixel
            blue=img[i,j,0]             #read BLUE_COLOR value of current pixel
            avg=min(red,green,blue)/2+max(red,green,blue)/2
            img[i,j]=avg                #Feed the GRAY value in current pixel
#    cv2.imshow("demo_gray",img)              #Show the result image (for testing only)



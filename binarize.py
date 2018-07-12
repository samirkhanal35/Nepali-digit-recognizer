def bin_(num1,num2,img):
#    import image as img
    import cv2
    import numpy as np
    import math
#    print (widthx,heighty,channel)
    for i in range(1,num1-1):
        for j in range(1,num2-1):
            gray=np.mean(img[i,j])
            if gray<=128:
                img[i,j]=0
            else:
                img[i,j]=255
        

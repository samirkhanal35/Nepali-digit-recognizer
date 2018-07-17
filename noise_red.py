def noisered(heighty,widthx,img):
    import cv2
    import math
    import numpy as np


    a=0
    b=0
    for h in range(1,heighty-1):   
        
        b=0
        for w in range(1,widthx-1):
            q=[]
            
            for i in range(-1,2):
                for j in range(-1,2):
                    aas=np.mean(img[h+i,w+j])    
                    q.append(aas)
            q.sort()
            value=q[4]
            #for i in range(a,h):
            #for j in range(b,w):
            img[h,w]=value
            b=w
        a=h


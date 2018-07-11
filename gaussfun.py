def gauss(heighty,widthx,img):
    import math
    import numpy as np
    pi=3.1416
    sigma=1.802
    a=0
    b=0
    for h in range(4,heighty):
        b=0
        for w in range(4,widthx):
            x=h-4
            y=w-4
            q=[]
            for i in range(a,h):
                for j in range(b,w):
                    d=((-1)*((i-x)**2+(j-y)**2))/(2*(sigma**2))
                    p=math.exp(d)
                    g=p/(2*pi*(sigma**2))
                    G=g*img[i,j]
                    q.append(G)           
            value=np.sum(q)
            img[x,y]=value    
            b=b+1
        a=a+1

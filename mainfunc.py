def main():
    import cv2
    import image as img
    import gary_convert as gc
    import noise_red as nr
    import binarize as br
    import gaussfun as gau
    import segment as sg
    from tkinter import filedialog
    fileName=filedialog.askopenfilename(filetypes=(("JPEG","*.jpg"),("PNG","*.png"),("All Files","*.*")))  
    img=cv2.imread(fileName)
    img1=img
    heighty,widthx,ch=img.shape
    print(ch)
    th=heighty
    tw=widthx
    if ((heighty>800) | (widthx>800)):
        if ((heighty>800) & (widthx<800)):
            r=heighty/widthx
            h=800
            hd=heighty-800
            wd=widthx-hd/r
            w=int(wd)
        if ((heighty<800) & (widthx>800)):
            r=widthx/heighty
            w=800
            wd=widthx-800
            hd=heighty-wd/r
            h=int(hd)
        if ((heighty>800) & (widthx>800)):
            if (heighty>=widthx):
                r=heighty/widthx
                h=800
                hd=heighty-800
                wd=widthx-hd/r
                w=int(wd)
            else:
                r=widthx/heighty
                w=800
                wd=widthx-800
                hd=heighty-wd/r
                h=int(hd)
                
                
        #dst = cv2.resize(img, (w, h), interpolation = cv2.INTER_CUBIC)
        #cv2.imshow("demo1",dst)
        heighty,widthx,ch=dst.shape
        gc.gray_con(heighty,widthx,dst)
        print("Grayed")
        nr.noisered(heighty,widthx,dst)
        print("filtered")
        #img1=cv2.resize(dst,(tw,th),interpolation = cv2.INTER_CUBIC)
        #gau.gauss(heighty,widthx,dst)
        print("Blurred")
        
        br.bin_(heighty,widthx,dst)
        print("Binarized")
        sg.segFun(heighty,widthx,dst)
        print("Segmented")
        cv2.imshow("demo2",dst)
    else:
        cv2.imshow("demo1",img)
        gc.gray_con(heighty,widthx,img)
        print("Grayed")
        nr.noisered(heighty,widthx,img)
        print("filtered")
        #gau.gauss(heighty,widthx,img)
        print("Blurred")
        br.bin_(heighty,widthx,img)
        print("Binarized")
        sg.segFun(heighty,widthx,img)
        print("Segmented")
        cv2.imshow("demo2",img)        

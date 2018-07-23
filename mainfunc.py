def main(img,heighty,widthx,ch):
    import cv2
    #from PIL import Image,ImageTk
    import gary_convert as gc
    import noise_red as nr
    import binarize as br
    import gaussfun as gau
    import segment as sg

    c=[]

    print(ch)
    #cv2.imshow("demo1",img)
    gc.gray_con(heighty,widthx,img)
    print("Grayed")
    nr.noisered(heighty,widthx,img)
    print("filtered")
    #gau.gauss(heighty,widthx,img)
    print("Blurred")
    br.bin_(heighty,widthx,img)
    print("Binarized")
    c=sg.segFun(heighty,widthx,img)
    print(c)
    return (c)

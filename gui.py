import tkinter as tk
from tkinter import filedialog
#import tkFileDialog as filedialog
import cv2
from PIL import Image,ImageTk
import image
from mainfunc import main
top = tk.Tk()
top.title("Nepali Digit Recognizer")
top.geometry("600x600")
#top.iconbitmap(r'npc_win.ico')
#img2 =ImageTk.PhotoImage(file='npc_win.ico')
#top.tk.call('wm', 'iconphoto', top._w, img2)
top.resizable(0,0)
#***********************************************************
class variables():
    fileName=str
    heighty=int
    widthx=int
    ch=int
    img=image
    frame2 = tk.Frame(top,bg="", width="600", height="400", colormap="new")
    frame2.grid(row=1,column=0)
    frame2.pack_propagate(0)
    L=tk.Label(frame2,text="Your input will appear here")
    L.grid()
    count=0
#***********************************************************
def design_fun():
    choose_but = tk.Button(top,text ="Choose image",command=choose)
    choose_but.grid(row=0,column=0)
    start_but=tk.Button(top,text="Start",command=call_main)
    start_but.grid(row=2,column=0)

    exit_but = tk.Button(top,text ="Exit",command=call_exit)
    exit_but.grid(row=3,column=0)
#***********************************************************
def call_exit():
    exit(0)
#***********************************************************
def choose():
    variables.fileName=""
    variables.L.grid_forget()
    variables.fileName=filedialog.askopenfilename(filetypes=(("JPEG","*.jpg"),
                                                   ("PNG","*.png"),
                                                   ("All Files","*.*")))

    if (variables.fileName!=""):
        variables.img=cv2.imread(variables.fileName)
        variables.heighty,variables.widthx,variables.ch=variables.img.shape

        img1=Image.open(variables.fileName)
        ph1=resize_img(img1,variables.widthx,variables.heighty)
        ph = ImageTk.PhotoImage(ph1)
        variables.L=tk.Label(variables.frame2,image=ph)
        variables.L.image=ph
        variables.L.pack(anchor="n")

#***********************************************************
def call_main():
    if (variables.fileName!=""):
        cv2.imshow("call_main",variables.img)
        main(variables.img,variables.heighty,variables.widthx,variables.ch)
#***********************************************************
def resize_img(img,widthx,heighty):
    th=heighty
    tw=widthx
    if ((heighty>400) | (widthx>600)):
        if ((heighty>400) & (widthx<600)):
            r=heighty/widthx
            h=400
            hd=heighty-400
            wd=widthx-hd/r
            w=int(wd)
        if ((heighty<400) & (widthx>600)):
            r=widthx/heighty
            w=600
            wd=widthx-600
            hd=heighty-wd/r
            h=int(hd)
        if ((heighty>400) & (widthx>600)):
            if (heighty>=widthx):
                r=heighty/widthx
                h=400
                hd=heighty-400
                wd=widthx-hd/r
                w=int(wd)
            else:
                r=widthx/heighty
                w=600
                wd=widthx-600
                hd=heighty-wd/r
                h=int(hd)
        img = img.resize((w, h), Image.ANTIALIAS)
    return img
#***********************************************************
design_fun()


top.mainloop()


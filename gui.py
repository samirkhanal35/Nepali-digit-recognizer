import tkinter as tk
from mainfunc import main
top = tk.Tk()

B = tk.Button(top, text ="Choose image",command=main)
B.pack()

top.mainloop()

from tkinter import *

#initializing Tkinter & Setting Window
fkt=Tk()
fkt.geometry("350x400")
fkt.title("Simple Calculator With Voice")
fkt.iconbitmap("calculator.ico")
C = Canvas(fkt, bg="gray", height=80, width=350)
C.pack()


fkt.mainloop()
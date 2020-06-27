from tkinter import *
import core_class

def press(key):
    print("You Pressed "+ key)


def set_buttons():
    cont = ["OK", "1"]
    for x in cont:
        but = Button(text=x, width=8, height=3, padx=2, pady=2, relief=RIDGE, command=press(x))
        but.pack()

#initializing Tkinter & Setting WindowRIDGE
fkt=Tk()
fkt.geometry("350x400")
fkt.title("Simple Calculator With Voice")
fkt.iconbitmap("calculator.ico")
fkt.configure(bg="white")
C = Canvas(fkt, bd=2, bg="gray", height=80, width=340)
C.pack()

set_buttons()



fkt.mainloop()
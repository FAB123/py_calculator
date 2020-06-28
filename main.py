from tkinter import *
from py_calculator.calc_core import calc_core

class calculator():
    # initializing Tkinter & Setting WindowRIDGE
    fkt = Tk()
    fkt.geometry("375x570")
    fkt.title("Simple Calculator With Voice")
    fkt.iconbitmap("calculator.ico")
    fkt.configure(bg="white")
    fkt.resizable(0, 0)

    #call core engine
    engine = calc_core()
    engine.dispaly(fkt)
    engine.set_buttons()

    #call Gui
    fkt.mainloop()

from tkinter import *
import core_class

class calculator(core_class.calc_core):
    # initializing Tkinter & Setting WindowRIDGE
    fkt = Tk()
    fkt.geometry("375x570")
    fkt.title("Simple Calculator With Voice")
    fkt.iconbitmap("calculator.ico")
    fkt.configure(bg="white")
    fkt.resizable(0, 0)
    #Set Welcome Screen
    C = Canvas(fkt, bd=2, bg="gray", height=80, width=340)
    C.create_text(240, 40, font=("Purisa", 30), justify=RIGHT, text="Hello World!")
    C.delete(ALL)
    C.create_text(240, 40, font=("Purisa", 30), text="Hi!", justify=RIGHT)
    C.grid(rowspan=1, columnspan=5, padx=1, pady=15)

    #call core engine
    engine = core_class.calc_core()
    engine.set_buttons()
    #call Gui
    fkt.mainloop()

from tkinter import *
import pyttsx3

class calc_core:
    def __init__(self):
        self.keys = "0"

    def dispaly(self, fkt):
        # Set Welcome Screen
        self.C = Canvas(fkt, bd=2, bg="gray", height=80, width=340)
        self.C.create_text(250, 40, font=("Purisa", 30), justify=RIGHT, text="Hello World!")
        self.C.grid(rowspan=1, columnspan=5, padx=1, pady=15)

    #get key press
    def say(self, key):
        sound = pyttsx3.init()
        sound.say(key)
        sound.setProperty('rate', 10)
        sound.runAndWait()

    def press_me(self, key):
        print("You Pressed " + str(key))
        if self.keys == "0":
            self.keys = str(key)
            print(str(key))
        else:
           self.keys = str(self.keys) + str(key)
           print(str(key))
        self.C.delete(ALL)
        self.C.create_text(240, 40, font=("Purisa", 30), text=self.keys, justify=RIGHT)
        #self.say(key)

    #set Buttons
    def set_buttons(self):
        keys = ["ON", "AC", "%", "/", "7", "8", "9", "X", "4", "5", "6", "-", "1", "2", "3", "+", ".", "0", "sum"]
        n_row, n_col, t_row = 1, 0, 1
        for x in keys:
            if x == 'sum':
                buttons = Button(text="=", width=13, height=3, relief=RIDGE, font=("Courier New", 8, 'bold'), bd=2,
                                 command=lambda: self.press_me('equal'))
                buttons.config(font=('Courier New', 16, 'bold'), bg='#ffbf00', fg="white")
                buttons.grid(row=n_row, column=n_col, columnspan=2, pady=3, padx=3)
            else:
                buttons = Button(text=x, width=7, height=3, relief=RIDGE, font=("Courier New", 8, 'bold'), bd=2, command=lambda x=x: self.press_me(x))
                buttons.config(font=('Courier New', 14, 'bold'), bg='#ffe699', fg="#ff00ff")
                buttons.grid(row=n_row, column=n_col, pady=3, padx=3)
                if n_col == 3:
                    buttons.config(font=('Courier New', 14, 'bold'), bg='#ffbf00', fg="white")
                    n_row, t_row, n_col = 2 + t_row, t_row + 1, 0
                else:
                    n_col = n_col + 1
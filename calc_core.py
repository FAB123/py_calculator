from tkinter import *
import pyttsx3
import math

class calc_core:
    def __init__(self):
        self.keys = "0"
        self.result = "0"
        self.screen = "0"
        self.sound = pyttsx3.init()
        self.sound.setProperty('rate', 150)

    #get screen value
    def screen_text(self):
        return self.C.itemcget(ALL, 'text')

    #resize screen
    def resize(self, fkt):
        if self.screen == "0":
            fkt.geometry("560x590")
            self.screen = "1"
        else:
            fkt.geometry("375x590")
            self.screen = "0"
        self.update_dispaly(self.screen_text())

    #scan enter key
    def callback(self, event):
        self.press_me("equal")

    #get keybord strock
    def keystrock(self, e):
        xz = e.char
        print (xz)
        if (xz.isnumeric()):
            self.press_me(xz)
        if xz == "*" or xz == "+" or xz == "-" or xz == "/":
            self.press_me(xz)

    # Set Welcome Screen
    def dispaly(self, fkt):
        self.C = Canvas(fkt, bd=4, bg="#8c8c89", height=80, width=340)
        self.C.create_text(340, 40, font=("Purisa", 30), anchor=E, justify=RIGHT, text="Welcome", tags = "display")
        self.C.grid(rowspan=1, columnspan=4, padx=1, pady=15)

    #update screen
    def update_dispaly(self, data):
        self.C.delete(ALL)
        if self.screen == "0":
            self.C.configure(width=340)
            self.C.create_text(340, 40, font=("Purisa", 30), text=data, anchor=E, justify=RIGHT)
            self.C.grid(columnspan=4)
        else:
            self.C.configure(width=540)
            self.C.create_text(535, 40, font=("Purisa", 30), text=data, anchor=E, justify=RIGHT)
            self.C.grid(columnspan=6)

    #tts updates
    def say(self, text):
        self.sound.say(text)
        self.sound.runAndWait()

    #core method
    def press_me(self, key):
        if key == "+" or key == "-" or key == "*" or key == "/" or key == "%" or key == "r" or key == "pie" or key == "^" or key == "e" or key == "!":
            if key == "+":
                self.operator = "add"
            elif key == "-":
                self.operator = "substract"
            elif key == "*":
                self.operator = "multiple"
            elif key == "/":
                self.operator = "divide"
            elif key == "%":
                self.operator = "percent"
            elif key == "r":
                self.operator = "root"
            elif key == "pie":
                self.operator = "pie"
            elif key == "^":
                self.operator = "exponentiation"
            elif key == "sin":
                self.operator = "sin"
            elif key == "e":
                self.operator = "e"
            elif key == "tan":
                self.operator = "tan"
            elif key == "cos":
                self.operator = "cos"
            elif key == "!":
                self.operator = "factorial"
            self.C.delete("opration")
            self.C.create_text(15, 40, font=("Purisa", 30), text=key, justify=RIGHT, tags = "opration")

            if self.result == "0":
                self.value1 = self.keys
            else:
                self.value1 = self.result
            self.keys = "0"

        elif key == "MR":
            self.value1 = "0"
            self.keys = "0"
            self.result = "0"
            self.update_dispaly(self.memory)

        elif key == "M-":
            self.memory = "0"
            self.update_dispaly("Memory Cleaned")

        elif key == "AC":
            self.value1 = "0"
            self.keys = "0"
            self.result = "0"
            self.update_dispaly("0.0")

        elif key == "ln":
            self.value1 = int(self.screen_text())
            self.result = math.log(self.value1)
            self.memory = "natural logarithm of " + str(self.value1) + " = " + str(self.result)
            self.update_dispaly(self.result)

        elif key == "sin":
            self.value1 = int(self.screen_text())
            self.result = math.sin(self.value1)
            self.memory = "sin of " + str(self.value1) + " = " + str(self.result)
            self.update_dispaly(self.result)

        elif key == "cos":
            self.value1 = int(self.screen_text())
            self.result = math.cos(self.value1)
            self.memory = "cos of " + str(self.value1) + " = " + str(self.result)
            self.update_dispaly(self.result)

        elif key == "tan":
            self.value1 = int(self.screen_text())
            self.result = math.tan(self.value1)
            self.memory = "tan of " + str(self.value1) + " = " + str(self.result)
            self.update_dispaly(self.result)


        elif key == "equal":
            if self.operator == "add":
                self.result = float(self.value1) + float(self.keys)
                self.memory = str(self.value1) + "+" + str(self.keys) + " = " + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)
            elif self.operator == "substract":
                self.result = float(self.value1) - float(self.keys)
                self.memory = str(self.value1) + " - " + str(self.keys) + " = " + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)
            elif self.operator == "multiple":
                self.result = float(self.value1) * float(self.keys)
                self.memory = str(self.value1) + " * " + str(self.keys) + " = " + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)
            elif self.operator == "divide":
                self.result = float(self.value1) / float(self.keys)
                self.memory = str(self.value1) + " / " + str(self.keys) + " = " + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)
            elif self.operator == "percent":
                self.result = float(self.value1) % float(self.keys)
                self.memory = str(self.value1) + " % " + str(self.keys) + " = " + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)
            elif self.operator == "root":
                self.result = float(self.keys) ** (1 / float(self.value1))
                self.memory = str(self.value1) + " root " + str(self.keys) + " = " + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)




            if str(self.tts_enabled.get()) == "1":
                self.say(self.memory)
        else:
            if self.keys == "0":
                self.keys = str(key)
            else:
                self.keys = str(self.keys) + str(key)
            self.update_dispaly(self.keys)

        if str(self.tts_enabled.get()) == "1":
            if key != "equal":
                print(key)
                self.say(key)

    #set Buttons
    def set_buttons(self, fkt):
        #keys = ["AC", "^", "r", "%","pie", "e", "sin","cos", "tan", "!", "ln", "mr", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", ".", "0", "sum"]
        #keys = ["AC", "MR", "Si", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", ".", "0", "sum"]
        keys = ["AC", "MR", "Fx", "/", "%", "r", "7", "8", "9", "*", "pie", "^", "4", "5", "6", "-", "sin", "e", "1", "2", "3", "+", "tan", "ln", ".", "0", "sum", "cos", "!"]
        n_row, n_col, t_row = 1, 0, 1
        for x in keys:
            if x == 'sum':
                buttons = Button(text="=", width=13, height=3, relief=RIDGE, font=("Courier New", 8, 'bold'), bd=2,
                                 command=lambda: self.press_me('equal'))
                buttons.config(font=('Courier New', 16, 'bold'), bg='#ffbf00', fg="white")
                buttons.grid(row=n_row, column=n_col, columnspan=2, pady=3, padx=3)
                n_col = n_col + 2
            elif x == 'Fx':
                buttons = Button(text=x, width=7, height=3, relief=RIDGE, font=("Courier New", 8, 'bold'), bd=2,
                                 command=lambda: self.resize(fkt))
                buttons.config(font=('Courier New', 14, 'bold'), bg='#ffe699', fg="#ff00ff")
                buttons.grid(row=n_row, column=n_col, pady=3, padx=3)
                if n_col == 5:
                    buttons.config(font=('Courier New', 14, 'bold'), bg='#ffbf00', fg="white")
                    n_row, t_row, n_col = 2 + t_row, t_row + 1, 0
                else:
                    n_col = n_col + 1
            else:
                buttons = Button(text=x, width=7, height=3, relief=RIDGE, font=("Courier New", 8, 'bold'), bd=2, command=lambda x=x: self.press_me(x))
                buttons.config(font=('Courier New', 14, 'bold'), bg='#ffe699', fg="#ff00ff")
                buttons.grid(row=n_row, column=n_col, pady=3, padx=3)
                if n_col == 3:
                    buttons.config(font=('Courier New', 14, 'bold'), bg='#ffbf00', fg="white")
                if n_col == 5:
                    #buttons.config(font=('Courier New', 14, 'bold'), bg='#ffbf00', fg="white")
                    n_row, t_row, n_col = 2 + t_row, t_row + 1, 0
                else:
                    n_col = n_col + 1

        #set check box
        self.tts_enabled = IntVar(value=1)
        C2 = Checkbutton(text="Enable Text to Speech", variable=self.tts_enabled, \
                         onvalue=1, offvalue=0, height=1, \
                         width=48)
        C2.grid(row=7, column=0, columnspan=4)
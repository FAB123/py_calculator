from tkinter import *
import pyttsx3

class calc_core:
    def __init__(self):
        self.keys = "0"
        self.result = "0"
        self.sound = pyttsx3.init()
        self.sound.setProperty('rate', 150)

    def callback(self, event):
        self.press_me("equal")

    def keystrock(self, e):
        xz = e.char
        print (xz)
        if (xz.isnumeric()):
            self.press_me(xz)
        if xz == "*" or xz == "+" or xz == "-" or xz == "/":
            self.press_me(xz)

    def dispaly(self, fkt):
        # Set Welcome Screen
        self.C = Canvas(fkt, bd=4, bg="#8c8c89", height=80, width=340)
        self.C.create_text(250, 40, font=("Purisa", 30), justify=RIGHT, text="Welcome", tags = "display")
        self.C.grid(rowspan=1, columnspan=5, padx=1, pady=15)

    def update_dispaly(self, data):
        self.C.delete(ALL)
        self.C.create_text(240, 40, font=("Purisa", 30), text=data, justify=RIGHT)

    #get key press
    def say(self, text):
        self.sound.say(text)
        self.sound.runAndWait()

    def press_me(self, key):
        if key == "+" or key == "-" or key == "*" or key == "/":
            if key == "+":
                self.operator = "add"
            elif key == "-":
                self.operator = "substract"
            elif key == "*":
                self.operator = "multiple"
            elif key == "/":
                self.operator = "divide"

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
                self.memory = str(self.value1) + " multipled By " + str(self.keys) + "Equal" + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)
            elif self.operator == "divide":
                self.result = float(self.value1) / float(self.keys)
                self.memory = str(self.value1) + " Divided By " + str(self.keys) + "Equal" + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)
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
    def set_buttons(self):
        keys = ["AC", "MR", "M-", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", ".", "0", "sum"]
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

        self.tts_enabled = IntVar(value=1)
        C2 = Checkbutton(text="Enable Text to Speech", variable=self.tts_enabled, \
                         onvalue=1, offvalue=0, height=1, \
                         width=48)
        C2.grid(row=7, column=0, columnspan=5)
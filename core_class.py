from tkinter import *
class calc_core:
    #get key press
    def press_me(self, key):
        print("You Pressed " + str(key))
        #C.create_text(100, 10, font="Verdana 10 bold", text="Hello World!" + key)
        display = Entry(fkt, font=("Helvetica", 16), borderwidth=0, relief=RAISED, justify=RIGHT)
        display.insert(0, key)
        display.grid(row=0, column=0, columnspan=5)


    #set Buttons
    def set_buttons(self):
        keys = ["ON", "AC", "%", "/", "7", "8", "9", "X", "4", "5", "6", "-", "1", "2", "3", "+", ".", "0", "sum"]
        n_row, n_col, t_row = 1, 0, 1
        for x in keys:
            if x == 'sum':
                buttons = Button(text="=", width=13, height=3, relief=RIDGE, font=("Courier New", 8, 'bold'), bd=2,
                                 command=lambda: self.press_me(sum))
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
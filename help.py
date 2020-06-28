from tkinter import *
import datetime

class ABC:
    root = Tk()
    root.title("Calculator")
    root.geometry('397x506')
    root.config(bg="DodgerBlue")
    root.resizable(0,0)

    def data(self, a):
        print(a)
        b = self.entry1.get()
        b=b.strip()
        b = b+a
        self.entry1.delete(0,END)
        self.entry1.insert(0,(str(b) +" "))

    def calculate(self):
        value = self.entry1.get()
        if value:
            value = eval(value)
            self.entry2.delete(0, END)
            self.entry2.insert(0,(str(value) +" "))
            print(value)
        else:
            self.entry2.delete(0, END)
            self.entry2.insert(0, 0)

    def clear(self):
        print("buton clicked data in", datetime.datetime.now())
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry2.insert(0, 0)



    def __init__(self):
        self.buttonheight = 65
        self.buttonwidth = 99.2
        self.button_background_color="white"
        self.button_foreground_color="green"

        self.entry1 = Entry(self.root, width=21, font=("Tahoma", "26"),justify=RIGHT)
        self.entry1.place(height=130, x=0, y=0)
        self.entry2 = Entry(self.root, width=21, font=("Tahoma", "26"), justify=RIGHT,borderwidth=0)
        self.entry2.place(height=50, x=0, y=130)

        self.c = Button(self.root, text="(", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("("))
        self.c.place(height=self.buttonheight, width=self.buttonwidth, x=0, y=180.7)

        self.of = Button(self.root, text=")", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data(")"))
        self.of.place(height=self.buttonheight, width=self.buttonwidth, x=self.buttonwidth, y=181)

        self.module = Button(self.root, text="%", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("%"))
        self.module.place(height=self.buttonheight, width=self.buttonwidth, x=self.buttonwidth + self.buttonwidth,
                          y=180.7)

        self.div = Button(self.root, text="/", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("/"))
        self.div.place(height=self.buttonheight, width=self.buttonwidth,
                       x=self.buttonwidth + self.buttonwidth + self.buttonwidth, y=180.7)

        # row 2
        self.b7 = Button(self.root, text="7", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("7"))
        self.b7.place(height=self.buttonheight, width=self.buttonwidth, x=0, y=180.7 + self.buttonheight)

        self.b8 = Button(self.root, text="8", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("8"))
        self.b8.place(height=self.buttonheight, width=self.buttonwidth, x=self.buttonwidth, y=180.7 + self.buttonheight)

        self.b9 = Button(self.root, text="9", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("9"))
        self.b9.place(height=self.buttonheight, width=self.buttonwidth, x=self.buttonwidth + self.buttonwidth,
                      y=180.7 + self.buttonheight)

        self.mul = Button(self.root, text="x", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color ,command=lambda: self.data("*"))
        self.mul.place(height=self.buttonheight, width=self.buttonwidth,
                       x=self.buttonwidth + self.buttonwidth + self.buttonwidth, y=180.7 + self.buttonheight)

        # row 3

        self.b4 = Button(self.root, text="4", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color, command=lambda: self.data("4"))
        self.b4.place(height=self.buttonheight, width=self.buttonwidth, x=0, y=180.7 + self.buttonheight * 2)

        self.b5 = Button(self.root, text="5", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("5"))
        self.b5.place(height=self.buttonheight, width=self.buttonwidth, x=self.buttonwidth,
                      y=180.7 + self.buttonheight * 2)

        self.b6 = Button(self.root, text="6", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("6"))
        self.b6.place(height=self.buttonheight, width=self.buttonwidth, x=self.buttonwidth + self.buttonwidth,
                      y=180.7 + self.buttonheight * 2)

        self.sub = Button(self.root, text="-", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("-"))
        self.sub.place(height=self.buttonheight, width=self.buttonwidth,
                       x=self.buttonwidth + self.buttonwidth + self.buttonwidth, y=180.7 + self.buttonheight * 2)

        # row 4

        self.b1 = Button(self.root, text="1", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("1"))
        self.b1.place(height=self.buttonheight, width=self.buttonwidth, x=0, y=180.7 + self.buttonheight * 3)

        self.b2 = Button(self.root, text="2", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("2"))
        self.b2.place(height=self.buttonheight, width=self.buttonwidth, x=self.buttonwidth,
                      y=180.7 + self.buttonheight * 3)

        self.b3 = Button(self.root, text="3", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("3"))
        self.b3.place(height=self.buttonheight, width=self.buttonwidth, x=self.buttonwidth + self.buttonwidth,
                      y=180.7 + self.buttonheight * 3)

        self.add = Button(self.root, text="+", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("+"))
        self.add.place(height=self.buttonheight, width=self.buttonwidth,
                       x=self.buttonwidth + self.buttonwidth + self.buttonwidth, y=180.7 + self.buttonheight * 3)

        # row 5

        self.plus_or_minus = Button(self.root, text="C", font=("Tahoma", "16", "bold"),fg="red", bg=self.button_background_color,command=self.clear)
        self.plus_or_minus.place(height=self.buttonheight, width=self.buttonwidth, x=0, y=180.7 + self.buttonheight * 4)

        self.b0 = Button(self.root, text="0", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("0"))
        self.b0.place(height=self.buttonheight, width=self.buttonwidth, x=self.buttonwidth,
                      y=180.7 + self.buttonheight * 4)

        self.dot = Button(self.root, text=".", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color, bg=self.button_background_color,command=lambda: self.data("."))
        self.dot.place(height=self.buttonheight, width=self.buttonwidth, x=self.buttonwidth + self.buttonwidth,
                       y=180.7 + self.buttonheight * 4)

        self.equal = Button(self.root, text="=", font=("Tahoma", "16", "bold"),fg=self.button_foreground_color,bg=self.button_background_color,command=self.calculate)
        self.equal.place(height=self.buttonheight, width=self.buttonwidth,
                         x=self.buttonwidth + self.buttonwidth + self.buttonwidth, y=180.7 + self.buttonheight * 4)



        self.root.mainloop()


if __name__ == "__main__":
    a = ABC()
from tkinter import *
import base64
import speech_recognition as sr
import pyttsx3
import math
import threading
import time



class Core:
    def __init__(self):
        self.keys, self.result, self.screen = "0", "0", "0"
        global keys
        keys = ["AC", "+/-", "Fx", "/", "%", "√", "7", "8", "9", "*", "pie", "^", "4", "5", "6", "-", "sin", "log", "1",
                "2", "3", "+", "tan", "ln", ".", "0", "sum", "cos", "!"]
        self.sound = pyttsx3.init()
        self.sound.setProperty('rate', 130)
        global buttons, flag
        # global flag
        buttons = {}
        global mylist
        mylist = []
        global pools
        pools = True


    # set Menus
    def set_menu(self, fkt):
        menu = Menu(fkt)
        fkt.config(menu=menu)
        theme = IntVar()

        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label="Help", command=self.help)
        filemenu.add_command(label="About", command=self.aboutprogram)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exitprogram)
        menu.add_cascade(label="File", menu=filemenu)

        theme_menu = Menu(menu, tearoff=0)
        theme_menu.add_radiobutton(label="Default", value=0, variable=theme, command=lambda: self.changetheme(1))
        theme_menu.add_radiobutton(label="Blue", value=1, variable=theme, command=lambda: self.changetheme(2))
        theme_menu.add_radiobutton(label="Purple", value=2, variable=theme, command=lambda: self.changetheme(3))
        theme_menu.add_radiobutton(label="Magenta", value=3, variable=theme, command=lambda: self.changetheme(4))
        theme_menu.add_radiobutton(label="High Contrast", value=4, variable=theme, command=lambda: self.changetheme(5))
        menu.add_cascade(label="Theme", menu=theme_menu)

    def aboutprogram(self):
        fkt = Toplevel()
        fkt.geometry("345x300")
        fkt.title("Simple Calculator With Voice")
        fkt.iconbitmap("calculator.ico")
        fkt.configure(bg="black")
        fkt.resizable(0, 0)
        about = "This my First Python Gui Program \nThe main aim of this program is help some one visually impaired. \n & i " \
                "want to give a special thanks to CROSSROADS team for all valuable supports \n      The best way to find " \
                "yourself is to lose yourself in the service of others.\n(Mahatma Gandhi) "
        msg = Message(fkt, text=about, anchor=CENTER, width=340, bg="black", fg="white")
        msg.config(font=('times', 14, 'italic'))
        msg.grid(row=0, column=0)

    def help(self):
        root = Toplevel()
        root.title("Basic Usage Help")
        root.iconbitmap("calculator.ico")
        root.resizable(0, 0)
        configfile = Text(root, wrap=WORD, width=50, height=35)
        with open("help.bin", 'r') as f:
            configfile.insert(INSERT, base64.b64decode(f.read()))
        configfile.pack(fill="none", expand=TRUE)
        root.mainloop()

    def exitprogram(self):
        exit()

    def changetheme(self, option=1):
        # theme = ["main_button_bg", "main_button_fg", "main_button_active_bg", "main_button_active_fg",
        # "spl_button_bg", "spl_button_fg", "spl_button_active_bg", "spl_button_active_fg"] orange
        if option == 1:
            theme = ["#ffbf00", "white", "#ffc61a", "white", "#ff9900", "white", "#ffa31a", "white"]

        # blue
        elif option == 2:
            theme = ["#00394d", "white", "#006080", "white", "#00131a", "white", "#000000", "white"]

        # purple
        elif option == 3:
            theme = ["#660066", "white", "#800080", "white", "#330033", "white", "#1a001a", "white"]

        # magenta
        elif option == 4:
            theme = ["#99003d", "white", "#800033", "white", "#ff0066", "white", "#ff1a75", "white"]

        # high Contrast
        elif option == 5:
            theme = ["black", "#40C090", "black", "#40C090", "black", "#40C090", "black", "#40C090"]
        n_col = 0
        for x in keys:
            if x == 'sum':
                buttons[x].config(bg=theme[4], fg=theme[5], activebackground=theme[6], activeforeground=theme[7])
                n_col = n_col + 2
            else:
                buttons[x].config(bg=theme[0], fg=theme[1], activebackground=theme[2], activeforeground=theme[3])
                if n_col == 3:
                    buttons[x].config(bg=theme[4], fg=theme[5], activebackground=theme[6],
                                      activeforeground=theme[7])
                    n_col = n_col + 1
                elif n_col == 5:
                    n_col = 0
                else:
                    n_col = n_col + 1

    # get screen value
    def screen_text(self):
        c_value = C.itemcget(ALL, 'text')
        if c_value == "Welcome":
            return "0"
        else:
            return C.itemcget(ALL, 'text')

    # resize screen
    def resize(self, fkt):
        if self.screen == "0":
            fkt.geometry("560x590")
            self.screen = "1"
        else:
            fkt.geometry("375x590")
            self.screen = "0"
        self.update_dispaly(self.screen_text())

    # scan enter key
    def callback(self, event):
        self.press_me("equal")

    # get keyboard strokes
    def keystrokes(self, e):
        xz = e.char
        print(xz)
        if (xz.isnumeric()):
            self.press_me(xz)
        if xz == "*" or xz == "+" or xz == "-" or xz == "/":
            self.press_me(xz)

    # Set Welcome Screen
    def dispaly(self, fkt):
        global C
        C = Canvas(fkt, bd=4, bg="#8c8c89", height=80, width=350)
        C.create_text(350, 40, font=("Purisa", 30), anchor=E, justify=RIGHT, text="Welcome", tags="display")
        C.grid(rowspan=1, columnspan=4, padx=0, pady=5)

    # update screen
    def update_dispaly(self, data):
        C.delete(ALL)
        if self.screen == "0":
            C.configure(width=350)
            C.create_text(350, 40, font=("Purisa", 30), text=data, anchor=E, justify=RIGHT)
            C.grid(columnspan=4)
        else:
            C.configure(width=540)
            C.create_text(540, 40, font=("Purisa", 30), text=data, anchor=E, justify=RIGHT)
            C.grid(columnspan=6)

    # tts updates
    def say(self, text):
        word_dict = {
            "*": "multiple",
            "-": "subtract",
            "/": "divide",
            "+/-": "plus or minus",
            "!": "factorial",
            "ln": "natural logarithm",
            "√": "squire root",
            "log": "logarithm"
        }

        if text in word_dict:
            text = word_dict[text]

        self.add_to_list = threading.Thread(target=self.add_to_voice_list, args=(text,), daemon=True)
        if (pools):
            self.say_from_list = threading.Thread(target=self.say_voice, daemon=True)
            self.add_to_list.start()
            self.say_from_list.start()
        else:
           self.add_to_list.start()


    def add_to_voice_list(self, text):
        mylist.append(text)

    def say_voice(self):
        global pools
        pools = False
        self.sound.startLoop(False)
        while mylist:
            try:
                self.sound.say(mylist[0])
                self.sound.iterate()
                del mylist[0]
            except:
                continue
        self.sound.endLoop()
        pools = True

    # core method
    def press_me(self, key):
        if key == "+" or key == "-" or key == "*" or key == "/" or key == "%" or key == "^" or key == "log":
            if key == "+":
                self.operator = "add"
                try:
                    if (self.value1):
                        self.result = float(self.value1) + float(self.keys)
                        self.memory = str(self.value1) + "+" + str(self.keys) + " = " + str(self.result)
                        self.value1 = self.result
                        self.update_dispaly(self.result)
                except:
                    print("new")
            elif key == "-":
                self.operator = "subtract"
            elif key == "*":
                self.operator = "multiple"
            elif key == "/":
                self.operator = "divide"
            elif key == "%":
                self.operator = "percent"
            elif key == "^":
                self.operator = "exponentiation"
            elif key == "log":
                self.operator = "log"
            C.delete("opration")
            C.create_text(15, 40, font=("Purisa", 30), text=key, justify=RIGHT, tags="opration")

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

        elif key == "AC":
            self.value1 = "0"
            self.keys = "0"
            self.result = "0"
            key = "Clear"
            self.update_dispaly("0.0")

        elif key == "ln":
            self.value1 = float(self.screen_text())
            self.result = math.log(self.value1)
            self.memory = "natural logarithm of " + str(self.value1) + " = " + str(self.result)
            self.update_dispaly(self.result)

        elif key == "√":
            self.value1 = float(self.screen_text())
            self.result = math.sqrt(self.value1)
            self.memory = "√ of " + str(self.value1) + " = " + str(self.result)
            self.update_dispaly(self.result)

        elif key == "pie":
            self.value1 = float(self.screen_text())
            self.result = float(self.value1) * math.pi
            self.memory = "pi of " + str(self.value1) + " = " + str(self.result)
            self.update_dispaly(self.result)

        elif key == "!":
            self.value1 = float(self.screen_text())
            if self.value1 < 0:
                self.update_dispaly("ERROR: Factorials allow only < 0")
            else:
                self.result = math.factorial(self.value1)
                self.memory = "factorial of " + str(self.value1) + " = " + str(self.result)
                self.update_dispaly(self.result)

        elif key == "sin":
            self.value1 = int(self.screen_text())
            self.result = math.sin(self.value1)
            self.memory = "sin of " + str(self.value1) + " = " + str(self.result)
            self.update_dispaly(self.result)

        elif key == "cos":
            self.value1 = float(self.screen_text())
            self.result = math.cos(self.value1)
            self.memory = "cos of " + str(self.value1) + " = " + str(self.result)
            self.update_dispaly(self.result)

        elif key == "tan":
            self.value1 = float(self.screen_text())
            self.result = math.tan(self.value1)
            self.memory = "tan of " + str(self.value1) + " = " + str(self.result)
            self.update_dispaly(self.result)

        elif key == "equal":
            if self.operator == "add":
                self.result = float(self.value1) + float(self.keys)
                self.memory = str(self.value1) + "+" + str(self.keys) + " = " + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)
            elif self.operator == "subtract":
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
                self.result = (float(self.value1) * float(self.keys)) / 100
                self.memory = str(self.value1) + " % " + str(self.keys) + " = " + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)
            elif self.operator == "root":
                self.result = float(self.keys) ** (1 / float(self.value1))
                self.memory = str(self.value1) + " root " + str(self.keys) + " = " + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)

            elif self.operator == "exponentiation":
                self.result = math.pow(float(self.value1), float(self.keys))
                self.memory = str(self.value1) + " root " + str(self.keys) + " = " + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)

            elif self.operator == "log":
                self.result = math.log(float(self.value1), float(self.keys))
                self.memory = "log of " + str(self.value1) + " base " + str(self.keys) + " = " + str(self.result)
                self.value1 = self.result
                self.update_dispaly(self.result)

            if str(tts_enabled.get()) == "1":
                self.say(self.memory)
        else:
            if key == "+/-":
                if self.keys != "0":
                    if int(self.keys) < 0:
                        self.keys = self.keys[1:]
                    else:
                        self.keys = "-" + self.keys[0:]
                else:
                    self.keys = "-"

            elif self.keys == "0":
                self.keys = str(key)

            else:
                self.keys = str(self.keys) + str(key)
            self.update_dispaly(self.keys)

        if str(tts_enabled.get()) == "1":
            if key != "equal":
                self.say(key)

    # set Buttons
    def set_buttons(self, fkt):
        n_row, n_col, t_row = 1, 0, 1

        for x in keys:
            if x == 'sum':
                buttons[x] = Button(text="=", width=13, height=3, relief=RIDGE, font=("Courier New", 8, 'bold'), bd=2,
                                    command=lambda: self.press_me('equal'))
                buttons[x].config(font=('Courier New', 16, 'bold'), bg='#ff9900', fg="white",
                                  activebackground="#ffa31a", activeforeground="white")
                buttons[x].grid(row=n_row, column=n_col, columnspan=2, pady=3, padx=3)
                n_col = n_col + 2
            elif x == 'Fx':
                buttons[x] = Button(text=x, width=7, height=3, relief=RIDGE, font=("Courier New", 8, 'bold'), bd=2,
                                    command=lambda: self.resize(fkt))
                buttons[x].config(font=('Courier New', 14, 'bold'), bg='#ffbf00', fg="white",
                                  activebackground="#ffc61a", activeforeground="white")
                buttons[x].grid(row=n_row, column=n_col, pady=3, padx=3)
                if n_col == 5:
                    n_row, t_row, n_col = 2 + t_row, t_row + 1, 0
                else:
                    n_col = n_col + 1
            else:
                buttons[x] = Button(text=x, width=7, height=3, relief=RIDGE, font=("Courier New", 8, 'bold'), bd=2,
                                    command=lambda x=x: self.press_me(x))
                buttons[x].config(font=('Courier New', 14, 'bold'), bg="#ffbf00", fg="white",
                                  activebackground="#ffc61a", activeforeground="white")
                if n_col == 3:
                    buttons[x].config(font=('Courier New', 14, 'bold'), bg='#ff9900', fg="white",
                                      activebackground="#ffa31a", activeforeground="white")
                buttons[x].grid(row=n_row, column=n_col, pady=3, padx=3)
                if n_col == 5:
                    n_row, t_row, n_col = 2 + t_row, t_row + 1, 0
                else:
                    n_col = n_col + 1

        # set check box
        global tts_enabled
        tts_enabled = IntVar(value=1)
        C2 = Checkbutton(text="Enable Text to Speech", variable=tts_enabled, \
                         onvalue=1, offvalue=0, height=1, \
                         width=48)
        C2.grid(row=7, column=0, columnspan=4)

    # internal process for voice recognition
    def get_voice_input(self):
        tts_enabled = IntVar(value=1)
        pools = IntVar(value=0)
        self.sound.say("To Start Voice Command Say Calculator or say exit to exit Voice Command Mode")
        self.sound.runAndWait()
        start = True
        while (start):
            if str(tts_enabled.get()) == "0":
                try:
                    if flag != 1:
                        C.delete("voice_command")
                        C.create_text(175, 75, font=("Purisa", 12), text="Voice Command Disabled!!", justify=RIGHT,
                                      tags="voice_command")
                    flag = 1
                    continue
                except:
                    continue
            else:
                flag = 0
                command = self.takecommand()
            if "exit" in command:
                self.say("Thank's for using our voice calculator!")
                self.exitprogram()
                break

            elif "calc" in command:
                notExit = True
                while (notExit):
                    command = self.takecommand()
                    if "quit" in command:
                        self.say("Thank's for using our voice calculator!")
                        break

                    elif str(tts_enabled.get()) == "0":
                        notExit = False
                        C.delete("voice_command")
                        C.create_text(175, 75, font=("Purisa", 12), text="Voice Command Disabled!!", justify=RIGHT,
                                      tags="voice_command")
                        break

                    elif command.isnumeric():
                        try:
                            self.press_me(command)
                        except:
                            self.say("Sorry try again!")

                    elif "clear" in command:
                        try:
                            self.press_me("AC")
                        except:
                            self.say("Sorry try again!")

                    elif "add" in command:
                        try:
                            self.press_me("+")
                        except:
                            self.say("Sorry try again!")
                    elif "equal" in command:
                        try:
                            self.press_me("equal")
                        except:
                            self.say("Sorry try again!")

                    elif "sub" in command:
                        try:
                            self.press_me("-")
                        except:
                            self.say("Sorry try again!")
                    elif "multi" in command:
                        try:
                            self.press_me("*")
                        except:
                            self.say("Sorry try again!")
                    elif "div" in command:
                        try:
                            self.press_me("/")
                        except:
                            self.say("Sorry try again!")

    def takecommand(self):
        # Returns string output from microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            C.delete("voice_command")
            C.create_text(175, 75, font=("Purisa", 12), text="Listening ...", justify=RIGHT, tags="voice_command")
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            try:
                audio = r.listen(source, timeout=1, phrase_time_limit=5)
            except:
                return "None"
        try:
            print("Recognizing ...")
            C.delete("voice_command")
            C.create_text(175, 75, font=("Purisa", 12), text="Recognizing ...", justify=RIGHT, tags="voice_command")
            query = r.recognize_google(audio, language='en-in')
            print(f"user: {query}")
        except:
            self.say("Say That again please")
            return "None"
        return query
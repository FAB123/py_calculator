import pyttsx3
import speech_recognition as sr
import threading
import multiprocessing
from tkinter import *
import calc_core

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    '''This function speaks the Text which is passed in audio argument'''
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    """Returns string output from microphone"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user: {query}")
    except:
        speak("Say That again please")
        return "None"
    return query


def options():
    speak("Which kind of operation would you like to perform?")
    speak("Addition, subtraction, multiplication or division")
    speak("Say Exit for close the calculator")


def gui_process(q):
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

def txt_process(q):
    speak("Hello There! welcome to the voice calculator developed by, Nishant The Programmer")
    notExit = True
    while (notExit):
        options()
        command = takeCommand()
        if "exit" in command:
            speak("Thank's for using our voice calculator!")
            break

        elif "add" in command:
            try:
                speak("What is your first operand?")
                a = int(takeCommand())
                speak("What is your second operand?")
                b = int(takeCommand())
                speak(f"Addition of {a} and {b} is " + str(a + b))
            except:
                speak("Sorry try again!")
        elif "subtraction" in command:
            try:
                speak("What is your first operand?")
                a = int(takeCommand())
                speak("What is your second operand?")
                b = int(takeCommand())
                speak(f"{a} minus {b} is " + str(a - b))
            except:
                speak("Sorry try again!")
        elif "multi" in command:
            try:
                speak("What is your first operand?")
                a = int(takeCommand())
                speak("What is your second operand?")
                b = int(takeCommand())
                speak(f"Multiplication of {a} and {b} is " + str(a * b))
            except:
                speak("Sorry try again!")
        elif "div" in command:
            try:
                speak("What is your first operand?")
                a = int(takeCommand())
                speak("What is your second operand?")
                b = int(takeCommand())
                if (b == 0):
                    speak(
                        "As all we know any value divide by zero is undefined so please give a valid second operand next time, Thanks!")
                    continue

                speak(f"{a} divide by {b} is " + str(a / b))
            except:
                speak("Sorry try again!")


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    # creating GUI process
    temp = 1
    p1 = multiprocessing.Process(target=gui_process, args=(queue,))
    # Start GUI process
    p1.start()

    # creating a new process
    p = multiprocessing.Process(target=txt_process, args=(queue,))
    # Starting the new process
    p.start()

    # Wait for the processes to finish
    queue.close()
    queue.join_thread()
    p.join()
    p1.join()


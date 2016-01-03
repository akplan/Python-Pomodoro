#!/usr/bin/python

import Tkinter
from Tkinter import *
import tkMessageBox
import threading

def main():
    top = Tk()
    global pomodoros
    pomodoros = 0
    Tkinter.Label(top, text="Number of pomodoros:").grid(row=1, column=1)
    text = Tkinter.Label(top, text="")
    text.grid(row=1, column=2)
    def pomoStart(pomo):
        tkMessageBox.showinfo("Pomodoro","Pomodoro is Over!")
        pomodoros = pomo + 1
        text.configure(text="%d" % (pomodoros))
        return

    t = threading.Timer(5.0,pomoStart,[pomodoros])
    button = Tkinter.Button(top, text ="Start Pomodoro", command=lambda: t.start()).grid(row=3,column=1)
    top.mainloop()

main()

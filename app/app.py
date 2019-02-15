#!/usr/bin/python3
# -*- coding: utf-8 -*-
import platform

PYTHON_VER = int(platform.python_version().split(".")[0])

if PYTHON_VER < 3:
    import Tkinter as tkinter
    import tkMessageBox
else:
    import tkinter
    from tkinter import messagebox as tkMessageBox

def calc(key=None):
    elements = "0123456789*/+-"

    if key == "=":
        if entry.get()[0] not in elements:
            entry.insert(tkinter.END, "first element not a number!")
            tkMessageBox.showerror("Error!", "You did enter not a number.")
        try:
            calc_enter = entry.get()
            calc_enter = calc_enter.replace("^", "**")

            result = eval(calc_enter)
            entry.delete(0, tkinter.END)
            entry.insert(tkinter.END, str(result))
        except ZeroDivisionError:
            entry.delete(0, tkinter.END)
            entry.insert(tkinter.END, "Error!")
            tkMessageBox.showerror("Error!", "Oops! Something went wrong.")
    
    if key == "c":
        entry.delete(0, tkinter.END)

    
    if key != "=" and key != "c":
        entry.insert(tkinter.END, key)

root = tkinter.Tk()
root.title("SimpleCalc")
root.resizable(width=False, height=False)

entry = tkinter.Entry(master=root, width=33)
entry.grid(row=0, column=0, columnspan=5)

btn_list = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "/", "0", "^", "c",
    "", "=", "", ""
]

row = 1
column = 0

for txt in btn_list:
    command = lambda x=txt: calc(x)
    tkinter.Button(master=root, text=txt, command=command, width=5).grid(row=row, column=column)

    column += 1
    if column > 3:
        column = 0
        row += 1

root.mainloop()

#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Calculator using Tkinter

from tkinter import *
from PIL import Image, ImageTk

def init_calc():
    r = Tk()
    r.title("Calculator")

    r.iconbitmap("C:\\Users\\Gaurvi\\Downloads\\Calculator_icon.ico")
    r.geometry("300x450")

    bg = ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\calc_background.jpg")
    label = Label(r, image=bg)
    label.place(x=0,y=0)

    e = Entry(r, width = 30, borderwidth = 10, font = ("Times", 10))
    e.grid(row = 0, column = 0, columnspan = 3, padx = 40, pady = 20)

    images = {
        "1": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\1.png"),
        "2": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\2.png"),
        "3": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\3.png"),
        "4": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\4.png"),
        "5": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\5.png"),
        "6": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\6.png"),
        "7": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\7.png"),
        "8": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\8.png"),
        "9": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\9.png"),
        "0": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\10.png"),
        "+": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\11.png"),
        "-": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\12.png"),
        "*": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\13.png"),
        "/": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\14.png"),
        "=": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\15.png"),
        "C": ImageTk.PhotoImage(file = "C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\16.png")
    }

    def click(no):
        cr = e.get()
        e.delete(0, END)
        e.insert(0, str(cr) + str(no))

    def add():
        f = e.get()
        global fnum
        global mat
        mat = "ADDITION"
        fnum = int(f)
        e.delete(0, END)

    def sub():
        f = e.get()
        global fnum
        global mat
        mat = "SUBRACTION"
        fnum = int(f)
        e.delete(0, END)

    def mul():
        f = e.get()
        global fnum
        global mat
        mat = "MULTIPLICATION"
        fnum = int(f)
        e.delete(0, END)

    def div():
        f = e.get()
        global fnum
        global mat
        mat = "DIVISION"
        fnum = int(f)
        e.delete(0, END)

    def eq():
        s = e.get()
        e.delete(0, END)

        if mat == "ADDITION":
            e.insert(0, fnum + int(s))
        if mat == "SUBRACTION":
            e.insert(0, fnum - int(s))
        if mat == "MULTIPLICATION":
            e.insert(0, fnum * int(s))
        if mat == "DIVISION":
            e.insert(0, fnum / int(s))

    def clr():
        e.delete(0, END)

    but = {
        "1" : (1,0,lambda: click(1)),
        "2" : (1,1,lambda: click(2)),
        "3" : (1,2,lambda: click(3)),
        "4" : (2,0,lambda: click(4)),
        "5" : (2,1,lambda: click(5)),
        "6" : (2,2,lambda: click(6)),
        "7" : (3,0,lambda: click(7)),
        "8" : (3,1,lambda: click(8)),
        "9" : (3,2,lambda: click(9)),
        "0" : (4,1,lambda: click(0)),
        "+" : (4,2,add),
        "-" : (4,0,sub),
        "*" : (5,1,mul),
        "/" : (5,0,div),
        "=" : (5,2,eq),
        "C" : (6,1,clr),
    }

    for btn, (row, col, cmd) in but.items():
        Button(r, border="3", image=images[btn], command=cmd).grid(row = row, column = col)

    r.images = images
    r.mainloop()

init_calc()


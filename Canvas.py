#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

groot = Tk()
#e=Entry(groot)
l= Label(groot, text="Groups!")
l.pack()
w = Canvas(groot, width=400, height=400)
w.pack()

w.create_rectangle(0, 0, 400, 400, fill="grey")

groot.mainloop()
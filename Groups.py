#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

class buttons:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.makeshape = Button(frame, text="Make Shape", command=self.printshape)
        self.triangleshape = Button(frame, text="Make a Triangle", command=self.triangleshape)
        self.makeshape.pack(side=LEFT)
        self.triangleshape.pack(side=LEFT)
    def printshape(self):
        print "hi there, everyone!"

    def triangleshape(self):
        print "make a triangle"

class shape():
    points=()
    shapetype=""
    color=""

    def __init__(self, shapetypestring, pointvector, colorstring):
        self.points = pointvector
        self.shapetype = shapetypestring
        self.color = colorstring

class MakeShapes(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)  

#        self.MakeCanvas(parent)
    
    #def MakeCanvas(self,parent):
        self.parent = parent     
        self.parent.title("Shapes")        
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=400, height=400)
        self.canvas.create_rectangle(0, 0, 400, 400, fill="grey")
        print "hello"
        self.MakeLabel()   
        #self.PlotShape("points",(25,25,100,100,75,100),"blue")

    def MakeLabel(self):
        self.pack(fill=BOTH, expand=1)
        label= Label(self, text="Groups!")
        label.pack(fill=BOTH,expand=1)

    def PlotShape(self,shape):
        if shape.shapetype == "rectangle":
            self.canvas.create_rectangle(shape.points[0], shape.points[1], shape.points[2], shape.points[3], fill=shape.color)
        if shape.shapetype == "oval":
            self.canvas.create_oval(shape.points[0], shape.points[1], shape.points[2], shape.points[3], fill=shape.color)
        if shape.shapetype == "points":
            self.canvas.create_polygon(shape.points, fill=shape.color)
        self.canvas.pack(fill=BOTH, expand=1)

#    def Rotate(self):

def main():
    groot = Tk()
    gps = MakeShapes(groot)
    button = buttons(groot)
    listofshapes=[]
    listofshapes.append(shape("points", (100,20,40,40,20,10), "red"))
    listofshapes.append(shape("rectangle", (200,20,40,40), "blue"))
    #print listofshapes
    #print len(listofshapes)
    for i in range(len(listofshapes)):
        MakeShapes.PlotShape(gps,listofshapes[i])
    groot.mainloop()


if __name__ == '__main__':
    main()
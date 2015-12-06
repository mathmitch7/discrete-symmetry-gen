#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import random

class shape():
    points=()
    shapetype=""
    color=""

    def __init__(self, shapetypestring, pointvector, colorstring):
        self.points = pointvector
        self.shapetype = shapetypestring
        self.color = colorstring

class MakeShapes(Frame):
    #canvas=Canvas()
  
    def __init__(self, parent):
        Frame.__init__(self, parent)  
        frame = Frame(parent)
        frame.grid()
        self.parent = parent     
        self.parent.title("Shapes")  

        self.listofshapes=[]
        self.makeshape = Button(frame, text="Make Shape", command=self.printshape).grid(row=5,column=0)
        self.symmetry = Button(frame, text="Make Symmetry!", command=self.symmetry).grid(row=6,column=0)
        self.clearall = Button(frame, text="Clear Shapes", command=self.clearshapes).grid(row=7,column=0)
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit).grid(row=8,column=0) 
        self.grouplabel = Label(frame, text="Symmetry Group:").grid(row=5,column=1)
        self.group = Entry(frame).grid(row=5,column=2)   

        self.shape=StringVar()
        self.color=StringVar()

        self.triangleoption = Radiobutton(frame,variable=self.shape,text="rectangle",value="rectangle").grid(row=6,column=1,sticky=W)
        self.ovaloption = Radiobutton(frame,variable=self.shape,text="oval",value="oval").grid(row=6,column=2,sticky=W)
        self.polygonoption = Radiobutton(frame,variable=self.shape,text="polygon",value="points").grid(row=6,column=3,sticky=W)
        self.blueoption = Radiobutton(frame,variable=self.color,text="blue",value="blue").grid(row=7,column=1,sticky=W)
        self.redoption = Radiobutton(frame,variable=self.color,text="red",value="red").grid(row=7,column=2,sticky=W)
        self.yellowoption = Radiobutton(frame,variable=self.color,text="yellow",value="yellow").grid(row=7,column=3,sticky=W)

        self.canvas = Canvas(frame, width=400, height=400,background="white")#.grid(row=2,column=0)
        print self.canvas
        self.canvas.grid(row=1,column=0,columnspan=6,rowspan=4)
        self.MakeLabel(frame)   

    def MakeLabel(self,frame):
        self.label= Label(frame, text="Groups!").grid(row=0,column=0,columnspan=4)
        #label.grid(fill=BOTH,expand=1)

    def clearshapes(self):
        print "Shapes Cleared"
        #ms = MakeShapes(master)
        self.canvas.delete(ALL)

    def printshape(self):
        print self.shape.get()
        print self.color.get()
        a=random.uniform(0,400)
        b=random.uniform(a,400)
        c=random.randint(0,400)
        d=random.randint(c,400)
        self.listofshapes=[]
        self.listofshapes.append(shape(self.shape.get(), (a,b,c,d), self.color.get()))
        print self.listofshapes
        #print len(listofshapes)
        for i in range(len(self.listofshapes)):
            self.PlotShape(self.listofshapes[i])

    def PlotShape(self,shape):
        #print "PRINT SHAPES"
        if shape.shapetype == "rectangle":
            self.canvas.create_rectangle(shape.points[0], shape.points[1], shape.points[2], shape.points[3], fill=shape.color)
        if shape.shapetype == "oval":
            self.canvas.create_oval(shape.points[0], shape.points[1], shape.points[2], shape.points[3], fill=shape.color)
        if shape.shapetype == "points":
            a=random.uniform(0,400)
            b=random.uniform(a,400)
            c=random.randint(0,400)
            d=random.randint(c,400)
            self.canvas.create_polygon(shape.points,a,b,c,d, fill=shape.color)
        self.canvas.grid(row=1,column=0,columnspan=2)

    def symmetry(self):
        print "MAKE SYMMETRY"
        
        center = 200,200
        angle = self.getangle() / start
        offset = complex(center[0], center[1])
        newxy = []
        for x, y in xy:
            v = angle * (complex(x, y) - offset) + offset
            newxy.append(v.real)
            newxy.append(v.imag)
        self.coords(polygon_item, *newxy)

    def getangle(self):
        center = 200,200
        dx = self.canvasx(event.x) - center[0]
        dy = self.canvasy(event.y) - center[1]
        try:
            return complex(dx, dy) / abs(complex(dx, dy))
        except ZeroDivisionError:
            return 0.0 # cannot determine angle

def main():
    groot = Tk()
    gps = MakeShapes(groot)
    #button = buttons(groot,gps)
    groot.mainloop()


if __name__ == '__main__':
    main()
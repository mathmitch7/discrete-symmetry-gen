#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *


class buttons:
    def __init__(self, master):

        frame = Frame(master)
        frame.grid()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit).grid(row=5,column=0)
        #self.button.grid(side=LEFT)

        self.makeshape = Button(frame, text="Make Shape", command=self.printshape).grid(row=3,column=0)
        self.symmetry = Button(frame, text="Make Symmetry!", command=self.symmetry).grid(row=4,column=0)
        #self.triangleshape = Button(frame, text="Make a Triangle", command=self.triangleshape)
        self.triangleoption = Radiobutton(frame,variable="shape",text="triangle",value="triangle").grid(row=3,column=1,sticky=W)
        self.ovaloption = Radiobutton(frame,variable="shape",text="oval",value="oval").grid(row=3,column=2,sticky=W)
        self.polygonoption = Radiobutton(frame,variable="shape",text="polygon",value="points").grid(row=3,column=3,sticky=W)
        self.blueoption = Radiobutton(frame,variable="color",text="blue",value="blue").grid(row=4,column=1,sticky=W)
        self.redoption = Radiobutton(frame,variable="color",text="red",value="red").grid(row=4,column=2,sticky=W)
        self.yellowoption = Radiobutton(frame,variable="color",text="yellow",value="yellow").grid(row=4,column=3,sticky=W)
        # self.makeshape.grid(side=LEFT)
        # #self.triangleshape.grid(side=LEFT)
        # self.triangleoption.grid(side=BOTTOM)
        # self.ovaloption.grid(side=BOTTOM)
        # self.polygonoption.grid(side=BOTTOM)
        # self.blueoption.grid(side=BOTTOM)
        # self.redoption.grid(side=LEFT)
        # self.yellowoption.grid(side=LEFT)

    def printshape(self):
        print "MAKE A SHAPE"

    def symmetry(self):
        print "MAKE SYMMETRY"

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
        frame = Frame(parent)
        frame.grid()
#        self.MakeCanvas(parent)
    
    #def MakeCanvas(self,parent):
        self.parent = parent     
        self.parent.title("Shapes")    
        self.canvas = Canvas(frame, width=400, height=400,background="white")#.grid(row=2,column=0)
        self.canvas.grid(row=1,column=0,columnspan=6,rowspan=4)
        #self.canvas.create_rectangle(0, 0, 400, 400, fill="grey")
        #print "hello"
        self.MakeLabel(frame)   
        #self.PlotShape("points",(25,25,100,100,75,100),"blue")

    def MakeLabel(self,frame):
        self.label= Label(frame, text="Groups!").grid(row=0,column=0,columnspan=4)
        #label.grid(fill=BOTH,expand=1)

    def PlotShape(self,shape):
        print "PRINT SHAPES"
        if shape.shapetype == "rectangle":
            self.canvas.create_rectangle(shape.points[0], shape.points[1], shape.points[2], shape.points[3], fill=shape.color)
        if shape.shapetype == "oval":
            self.canvas.create_oval(shape.points[0], shape.points[1], shape.points[2], shape.points[3], fill=shape.color)
        if shape.shapetype == "points":
            self.canvas.create_polygon(shape.points, fill=shape.color)
        self.canvas.grid(row=1,column=0,columnspan=2)

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
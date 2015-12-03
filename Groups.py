#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *


# class buttons:
#     def __init__(self, master,gps):

#         frame = Frame(master)
#         frame.grid()
        # self.listofshapes=[]
        # self.makeshape = Button(frame, text="Make Shape", command=self.printshape(gps)).grid(row=3,column=0)
        # self.symmetry = Button(frame, text="Make Symmetry!", command=self.symmetry).grid(row=4,column=0)
        # self.clearall = Button(frame, text="Clear Shapes", command=self.clearshapes(master)).grid(row=5,column=0)
        # self.button = Button(frame, text="QUIT", fg="red", command=frame.quit).grid(row=6,column=0)   

        # self.triangleoption = Radiobutton(frame,variable="shape",text="triangle",value="triangle").grid(row=3,column=1,sticky=W)
        # self.ovaloption = Radiobutton(frame,variable="shape",text="oval",value="oval").grid(row=3,column=2,sticky=W)
        # self.polygonoption = Radiobutton(frame,variable="shape",text="polygon",value="points").grid(row=3,column=3,sticky=W)
        # self.blueoption = Radiobutton(frame,variable="color",text="blue",value="blue").grid(row=4,column=1,sticky=W)
        # self.redoption = Radiobutton(frame,variable="color",text="red",value="red").grid(row=4,column=2,sticky=W)
        # self.yellowoption = Radiobutton(frame,variable="color",text="yellow",value="yellow").grid(row=4,column=3,sticky=W)

    # def clearshapes(self,master):
    #     print "Shapes Cleared"
    #     #ms = MakeShapes(master)
    #     MakeShapes.canvas.delete(ALL)

    # def printshape(self,gps):
    #     self.listofshapes=[]
    #     self.listofshapes.append(shape("points", (100,20,40,40,20,10), "red"))
    #     self.listofshapes.append(shape("rectangle", (200,20,40,40), "blue"))
    #     #print listofshapes
    #     #print len(listofshapes)
    #     for i in range(len(self.listofshapes)):
    #         MakeShapes.PlotShape(gps,self.listofshapes[i])

    # def symmetry(self):
    #     print "MAKE SYMMETRY"

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

        self.triangleoption = Radiobutton(frame,variable="shape",text="triangle",value="triangle").grid(row=6,column=1,sticky=W)
        self.ovaloption = Radiobutton(frame,variable="shape",text="oval",value="oval").grid(row=6,column=2,sticky=W)
        self.polygonoption = Radiobutton(frame,variable="shape",text="polygon",value="points").grid(row=6,column=3,sticky=W)
        self.blueoption = Radiobutton(frame,variable="color",text="blue",value="blue").grid(row=7,column=1,sticky=W)
        self.redoption = Radiobutton(frame,variable="color",text="red",value="red").grid(row=7,column=2,sticky=W)
        self.yellowoption = Radiobutton(frame,variable="color",text="yellow",value="yellow").grid(row=7,column=3,sticky=W)

        self.canvas = Canvas(frame, width=400, height=400,background="white")#.grid(row=2,column=0)
        print self.canvas
        self.canvas.grid(row=1,column=0,columnspan=6,rowspan=4)
        self.MakeLabel(frame)   

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

    def clearshapes(self):
        print "Shapes Cleared"
        #ms = MakeShapes(master)
        self.canvas.delete(ALL)

    def printshape(self):
        self.listofshapes=[]
        self.listofshapes.append(shape("points", (100,20,40,40,20,10), "red"))
        self.listofshapes.append(shape("rectangle", (200,20,40,40), "blue"))
        #print listofshapes
        #print len(listofshapes)
        for i in range(len(self.listofshapes)):
            self.PlotShape(self.listofshapes[i])

    def symmetry(self):
        print "MAKE SYMMETRY"

#    def Rotate(self):

def main():
    groot = Tk()
    gps = MakeShapes(groot)
    #button = buttons(groot,gps)
    groot.mainloop()


if __name__ == '__main__':
    main()
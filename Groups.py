#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import random
import math

class shape():
    points=()
    shapetype=""
    color=""

    def __init__(self, shapetypestring, pointvector, colorstring):
        self.points = pointvector
        self.shapetype = shapetypestring
        self.color = colorstring
        self.rotationalgen = 0

class MakeShapes(Frame):
    #canvas=Canvas()
  
    def __init__(self, parent):
        Frame.__init__(self, parent)  
        frame = Frame(parent)
        frame.grid()
        self.parent = parent     
        self.parent.title("Shapes")
        self.listofshapes=[]  

        self.listofshapes=[]
        self.makeshape = Button(frame, text="Make Shape", command=self.printshape).grid(row=5,column=0)
        self.symmetry = Button(frame, text="Make Symmetry!", command=self.symmetry).grid(row=6,column=0)
        self.clearall = Button(frame, text="Clear Shapes", command=self.clearshapes).grid(row=7,column=0)
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit).grid(row=8,column=0) 
        self.grouplabel = Label(frame, text="Symmetry Group:").grid(row=5,column=1)
        self.group = Entry(frame)
        self.group.grid(row=5,column=2)   

        self.shape=StringVar()
        self.color=StringVar()
        self.symmetrytype=StringVar()

        self.shapelabel = Label(frame, text="Shape Type:").grid(row=6,column=1)
        self.ovaloption = Radiobutton(frame,variable=self.shape,text="circle",value="circle").grid(row=6,column=3,sticky=W)
        self.polygonoption = Radiobutton(frame,variable=self.shape,text="polygon",value="polygon").grid(row=6,column=4,sticky=W)

        self.colorlabel = Label(frame, text="Shape Color:").grid(row=7,column=1)
        self.blueoption = Radiobutton(frame,variable=self.color,text="blue",value="blue").grid(row=7,column=2,sticky=W)
        self.redoption = Radiobutton(frame,variable=self.color,text="red",value="red").grid(row=7,column=3,sticky=W)
        self.yellowoption = Radiobutton(frame,variable=self.color,text="yellow",value="yellow").grid(row=7,column=4,sticky=W)

        self.symmetrylabel = Label(frame, text="Symmetry:").grid(row=8,column=1)
        self.rotationoption = Radiobutton(frame,variable=self.symmetrytype,text="rotation",value="rotation").grid(row=8,column=2,sticky=W)
        self.reflectionoption = Radiobutton(frame,variable=self.symmetrytype,text="reflection",value="reflection").grid(row=8,column=3,sticky=W)
        self.completeoption = Radiobutton(frame,variable=self.symmetrytype,text="complete",value="complete").grid(row=8,column=4,sticky=W)

        self.canvas = Canvas(frame, width=400, height=400,background="white")
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
        self.listofshapes=[]

    def printshape(self):
        print self.shape.get()
        print self.color.get()
        points=[]
        if self.shape.get() == "circle":
            a=random.uniform(0,300)
            b=random.uniform(a,300)
            size=random.uniform(10,100)
            c=a+size
            print c
            d=b+size
            points.append(a)
            points.append(b)
            points.append(c)
            points.append(d)
        if self.shape.get() == "polygon":
            numberofpts = random.randint(3,6)
            for i in range(0,numberofpts):
                a=random.uniform(0,400)
                b=random.uniform(0,400)
                points.append(a)
                points.append(b)
        self.listofshapes.append(shape(self.shape.get(), (points), self.color.get()))
        #print self.listofshapes
        #print len(listofshapes)
        for i in range(len(self.listofshapes)):
            self.PlotShape(self.listofshapes[i])

    def PlotShape(self,shape):
        #print "PRINT SHAPES"
        if shape.shapetype == "circle":
           self.canvas.create_oval(shape.points[0], shape.points[1], shape.points[2],shape.points[3], fill=shape.color)
        if shape.shapetype == "polygon":
            self.canvas.create_polygon(shape.points, fill=shape.color)
            print "points"
            print shape.points
        self.canvas.grid(row=1,column=0,columnspan=2)

    def symmetry(self):
        #print "MAKE SYMMETRY"
        self.symmetrygrouptext = self.group.get()
        #print "Symmetry Group"
        #print self.symmetrygrouptext

    def angleofrotation(self, n): #takes a number  of rotational symmetry we want and spits out the number for the rotational generator
        self.rotationalgen = 2*math.pi / n
        return self.rotationalgen

    def linesofsymmetry(self, n): #takes a number  of reflective symmetry we want and spits out a list of the angles of the lines of symmetry
        self.symlines = []
        for i in range(n):
            self.symlines.append(i*math.pi / n)
        return self.symlines

    def findduplicates(self):
    	no_duplicates = []
    	for i in self.listofshapes:
    		if i not in no_duplicates:
    			no_duplicates.append(i)
		return no_duplicates

def rotatepoints(points, theta, origin=[0,0]):
    #takes [x0,y0,x1,y1 ...], an angle in rads, and a rotational origin as [x,y], returns a list in the same style as the first.
    rotatedPolygon = []
    print points[::2]
    for i in range(len(points)/2):
        rotatedPolygon.append((points[2*i]-origin[0])*math.cos(theta)-(points[2*i+1]-origin[1])*math.sin(theta)+origin[0])
        rotatedPolygon.append((points[2*i]-origin[0])*math.sin(theta)+(points[2*i+1]-origin[1])*math.cos(theta)+origin[1])
    return rotatedPolygon #this is a list btw

def flippoints(points, theta, origin=[0,0]):
    #takes [x0,y0,x1,y1 ...], an angle in rads, and a reflectional angle over which we want to reflect shit, that goes through the
    #origin as [x,y], returns a list in the same style as the first.
    # reflectedPolygon = []
    # print points[::2]
    # for i in range(len(points)/2):
    #     reflectedPolygon.append((points[2*i]-origin[0])
    #     rotatedPolygon.append((points[2*i]-origin[0])*math.cos(theta)-(points[2*i+1]-origin[1])*math.sin(theta)+origin[0])
    #     rotatedPolygon.append((points[2*i]-origin[0])*math.sin(theta)+(points[2*i+1]-origin[1])*math.cos(theta)+origin[1])
    # return rotatedPolygon #this is a list btw
    return

def main():
    groot = Tk()
    grps = MakeShapes(groot)
    #button = buttons(groot,grps)
    groot.mainloop()
    print rotatepoints([110,100,120,100,130,100],math.pi/2,[100,100])

if __name__ == '__main__':
    main()
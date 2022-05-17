#!/usr/bin/env python3
import turtle as tl
import numpy as np

def ellipse(a,b,x0,y0,theta0,color,opt=False):
    R = lambda l, e, theta: l/(1-e*np.cos(theta/180*np.pi))
    c = np.sqrt(a**2-b**2)
    e = c/a
    l = b**2/a
    tl.pensize(2)
    tl.color(color)
    if opt:
        tl.begin_fill()
    tl.penup()
    for i, theta in enumerate(np.linspace(0,360,100)):
        if i==1:
            tl.pendown()
        r = R(l,e,theta)
        x = r*np.cos((theta-theta0)/180*np.pi)-c*np.cos(theta0/180*np.pi)+x0
        y = r*np.sin((theta-theta0)/180*np.pi)+c*np.sin(theta0/180*np.pi)+y0
        tl.goto(x,y)
    if opt:
        tl.end_fill()

if __name__=='__main__':
    tl.screensize(801,801)
    tl.speed(10)
    #ear
    for th in [-1,1]:
        a, b, theta0,x0,y0,color  = 40, 30, -60*th, 130*th, 190, 'black'
        ellipse(a,b,x0,y0,theta0,color,True)
    
    #arm
    for th in [-1,1]:
        a, b, theta0,x0,y0,color  = 80, 40, -120*th, 210*th, -50, 'black'
        ellipse(a,b,x0,y0,theta0,color,True)
    
    #leg
    for th in [-1,1]:
        a, b, theta0,x0,y0,color  = 80, 50, 90, 80*th, -240, 'black'
        ellipse(a,b,x0,y0,theta0,color,True)
    
    
    #body
    for cl, opt in zip(['white','black'],[True,False]):
        a, b, theta0,x0,y0,color  = 230, 200, 90, 0, 0, cl
        ellipse(a,b,x0,y0,theta0,color,opt)
    
    #eye
    for th in [-1,1]:
        a, b, theta0,x0,y0,color  = 60, 40, 45*th, 80*th, 80, 'black'
        ellipse(a,b,x0,y0,theta0,color,True)
        a, b, theta0,x0,y0,color  = 10, 10, 45*th, 80*th, 80, 'white'
        ellipse(a,b,x0,y0,theta0,color,True)
        a, b, theta0,x0,y0,color  =  6,  6, 45*th, 80*th, 80, 'black'
        ellipse(a,b,x0,y0,theta0,color,True)
        a, b, theta0,x0,y0,color  =  1,  1, 45*th, 80*th, 80, 'white'
        ellipse(a,b,x0,y0,theta0,color,True)
    
    #nose
    a, b, theta0,x0,y0,color  = 20, 20, 90, 0, 40, 'black'
    ellipse(a,b,x0,y0,theta0,color,True)

    #mouse
    r = 30
    tl.penup()
    tl.goto(-1*r,0)
    tl.pendown()
    tl.right(90)
    tl.circle(r,180)
    

    for R,cl in zip(np.arange(145,151+5*7,5),['lime','green','yellow','red','purple','cyan','blue']):
        a, b, theta0,x0,y0,color  = R, R-10, 0, 0, 50, cl
        ellipse(a,b,x0,y0,theta0,color,False)

    tl.exitonclick()

# done by Alissar Salman and Abdullah Ayoub

import turtle as t

#sky
t.speed(0)
t.bgcolor("skyblue")

#house
h = 250
w = 370

def square():
    '''draws a square and is filled with the color sandybrown.'''

    t.speed(0)
    t.fillcolor("sandybrown")
    t.begin_fill()
    #starting position for the house
    t.penup()
    t.goto(-210,-270)
    t.pendown()
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.end_fill()
    #position
    t.penup()
    t.left(90)
    t.forward(h)
  
# roof1
def roof():
    '''draws a colored triangle and connects to the square.'''
    t.speed(0)
    t.fillcolor("darkred")
    t.begin_fill()
    t.left(-45)
    t.forward(260)
    t.left(-90)
    t.forward(260)
    t.left(225)
    t.forward(368)
    t.end_fill()

#door
def door():
    '''draws a colored door on the square to make a door to the house.'''
    #postion
    t.speed(0)
    t.left(90)
    t.penup()
    t.forward(h)
    t.left(90)
    t.forward(165)
    t.left(90)
    

    t.fillcolor("saddlebrown")
    t.begin_fill()
    t.forward(90)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.penup()
  
#left window
def lwin():
    '''draws one window to the left of the square to make one window for the house.'''

    #position
    t.forward(120)
    t.right(180)
    # win postion-
    t.speed(0)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.pendown()

    t.fillcolor("darkcyan")
    t.begin_fill()

    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)

    t.end_fill()

    #dividing 1/2
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)

    #dividing 1/4
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(100)
    
    t.penup()
 
 
#right window
def rwin():
    '''draws a window to the right on the square to make a second window for the house.'''

    #position
    t.forward(100)
    t.left(90)
    t.forward(190)

    #win position
    t.left(90)
    t.forward(100)

    t.pendown()

    t.fillcolor("darkcyan")
    t.begin_fill()

    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)

    t.end_fill()

    #dividing 1/2
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)

    #dividing 1/4
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(100)
    t.left(90)
    
    t.penup()

def main1():
    square()
    roof()
    door()
    lwin()
    rwin()

#sun
def circle():
    '''draws a circle to make the sun.'''

    t.speed(0)
    t.up()
    t.goto(-600,220)
    t.down()
    #sun position
    t.right(-90)

    t.pensize(3)
    t.pencolor("orange")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

#sunrays
def rays():
    '''draws lines to make sunrays'''
    for i in range(14):
        t.right(90)
        t.forward(40)
        t.backward(40)
        t.left(90)
        t.circle(50,30)

#cloud
def draw_cloud():
    '''draws four intersecting cirlces to make a cloud.'''
    t.speed(0)
    t.penup()
    t.goto(600,300)
    t.pendown()
    #cloud position
    t.right(-90)
   
    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    t.circle(35)
    t.end_fill()

    t.penup()
    t.goto(620,340)
    t.pendown()
    t.begin_fill()
    t.circle(35)
    t.end_fill()

    t.penup()
    t.goto(630,315)
    t.pendown()
    t.begin_fill()
    t.circle(35)
    t.end_fill()

    t.penup()
    t.goto(580,325)
    t.pendown()
    t.begin_fill()
    t.circle(35)
    t.end_fill()

def main3():
    circle()
    rays()
    draw_cloud()


#Grass
width = 1550
height = 130
def rectangle():
    '''draws a wide color filled rectangle to make the grass.'''
    t.goto(-780,-400)
    t.pendown()
    t.fillcolor("forestgreen")
    t.begin_fill()
    
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)

    t.end_fill()

def main2():
    rectangle()

    
###############################################################################################################################

def scenery():
    main1()
    main2()
    main3()

    t.done()

scenery()

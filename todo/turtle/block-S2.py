#! /usr/bin/env python3

"""
The second version of drawing the block S. 

I realized that in the first version it would 
make a lot more sense to have a list of points 
that Sparty could go to instead of messing with 
the lengths of the S. 

This makes it easy to scale either the x, or y coordinates. 
"""

#import the turtle module
#and be able to use the commands
import turtle

#list of points from start to end
DIAG=75

CAP_WIDTH=100
OUTSIDE_CAP=100
INSIDE_CAP=50
SMALL_INSIDE_WIDTH=200
LARGE_INSIDE_WIDTH=250
INSIDE_VERTICAL=100
OUTSIDE_VERTICAL=200
OUTSIDE_LINES=300

#make the "turtle object"
#this is our "turtle" that will
#run around the screen
sparty = turtle.Turtle()

#set the color to be THE spartan green
sparty.pencolor("#18453B")

#Put the pen "up" so that when we move we dont draw
sparty.penup()

#move sparty to the top left since that's where were starting
sparty.setx(-200)
sparty.sety(250)

#put the pen "down" so that we can start drawing
sparty.pendown()
print(sparty.position())

#Set the pen width
sparty.width(20)

#Draw the top part of the block S
sparty.forward(OUTSIDE_LINES)
sparty.position()

#right 45 degrees and draw the next part
sparty.right(45)
sparty.forward(DIAG)
sparty.position()

#drawing down
sparty.right(45)
sparty.forward(OUTSIDE_CAP)
sparty.position()

#drawing left
sparty.right(90)
sparty.forward(CAP_WIDTH)
sparty.position()

#draw up from the edge of the S
sparty.right(90)
sparty.forward(INSIDE_CAP)
sparty.position()

#angle back
sparty.left(90)
sparty.forward(SMALL_INSIDE_WIDTH)
sparty.position()

#draw down the inside of the top of the S
sparty.left(90)
sparty.forward(INSIDE_VERTICAL)
sparty.position()


#draw the middle of the S
sparty.left(90)
sparty.forward(LARGE_INSIDE_WIDTH)
sparty.position()

#angle down
sparty.right(45)
sparty.forward(DIAG)
sparty.position()

#angle down again
sparty.right(45)
sparty.forward(OUTSIDE_VERTICAL)
sparty.position()

#bottom right diag
sparty.right(45)
sparty.forward(DIAG)
sparty.position()

#bottom of S
sparty.right(45)
sparty.forward(OUTSIDE_LINES)
sparty.position()

#bottom left diag
sparty.right(45)
sparty.forward(DIAG)
sparty.position()

sparty.right(45)
sparty.forward(OUTSIDE_CAP)
sparty.position()

sparty.right(90)
sparty.forward(CAP_WIDTH)
sparty.position()

sparty.right(90)
sparty.forward(INSIDE_CAP)
sparty.position()

sparty.left(90)
sparty.forward(SMALL_INSIDE_WIDTH)
sparty.position()

#draw up the inside of the bottom of the S
sparty.left(90)
sparty.forward(INSIDE_VERTICAL)
sparty.position()

sparty.left(90)
sparty.forward(LARGE_INSIDE_WIDTH)
sparty.position()

#diag up
sparty.right(45)
sparty.forward(DIAG)
sparty.position()

#one last up
sparty.right(45)
sparty.forward(OUTSIDE_VERTICAL)
sparty.position()

#last line
sparty.right(45)
sparty.forward(DIAG)
sparty.position()



#waiting for user input to end the program
input()



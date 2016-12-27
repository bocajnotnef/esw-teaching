#! /usr/bin/env python3

"""
Draws a block S
"""

#import the turtle module
#and be able to use the commands
import turtle

#common widths for the block S
DIAG=75
OUTSIDE_LINES=300
OUTSIDE_CAP=100
INSIDE_CAP=50
CAP_WIDTH=100
SMALL_INSIDE_WIDTH=200
LARGE_INSIDE_WIDTH=250
INSIDE_VERTICAL=100
OUTSIDE_VERTICAL=200

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
sparty.sety(200)

#put the pen "down" so that we can start drawing
sparty.pendown()

#Set the pen width
sparty.width(20)

#Draw the top part of the block S
sparty.forward(OUTSIDE_LINES)

#right 45 degrees and draw the next part
sparty.right(45)
sparty.forward(DIAG)

#drawing down
sparty.right(45)
sparty.forward(OUTSIDE_CAP)

#drawing left
sparty.right(90)
sparty.forward(CAP_WIDTH)

#draw up from the edge of the S
sparty.right(90)
sparty.forward(INSIDE_CAP)

#angle back
sparty.left(90)
sparty.forward(SMALL_INSIDE_WIDTH)

#draw down the inside of the top of the S
sparty.left(90)
sparty.forward(INSIDE_VERTICAL)


#draw the middle of the S
sparty.left(90)
sparty.forward(LARGE_INSIDE_WIDTH)

#angle down
sparty.right(45)
sparty.forward(DIAG)

#angle down again
sparty.right(45)
sparty.forward(OUTSIDE_VERTICAL)

#bottom right diag
sparty.right(45)
sparty.forward(DIAG)

#bottom of S
sparty.right(45)
sparty.forward(OUTSIDE_LINES)

#bottom left diag
sparty.right(45)
sparty.forward(DIAG)

sparty.right(45)
sparty.forward(OUTSIDE_CAP)

sparty.right(90)
sparty.forward(CAP_WIDTH)

sparty.right(90)
sparty.forward(INSIDE_CAP)

sparty.left(90)
sparty.forward(SMALL_INSIDE_WIDTH)

#draw up the inside of the bottom of the S
sparty.left(90)
sparty.forward(INSIDE_VERTICAL)

sparty.left(90)
sparty.forward(LARGE_INSIDE_WIDTH)

#diag up
sparty.right(45)
sparty.forward(DIAG)

#one last up
sparty.right(45)
sparty.forward(OUTSIDE_VERTICAL)

#last line
sparty.right(45)
sparty.forward(DIAG)




#waiting for user input to end the program
input()



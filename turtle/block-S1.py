#! /usr/bin/env python3

"""
Draws a block S
"""

#import the turtle module
#and be able to use the commands
import turtle

#common widths for the block S
#changing these will change how the S is constructed
DIAG=75

OUTSIDE_CAP=100
INSIDE_CAP=50
CAP_WIDTH=100

OUTSIDE_WIDTH=300
SMALL_INSIDE_WIDTH=200
LARGE_INSIDE_WIDTH=250

INSIDE_VERTICAL=125
OUTSIDE_VERTICAL=225

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

#Set the pen width
sparty.width(20)

#Draw the top part of the block S
sparty.forward(OUTSIDE_WIDTH)

#rotate right 45 degrees and draw the diag down
sparty.right(45)
sparty.forward(DIAG)

#drawing on the right side
sparty.right(45)
sparty.forward(OUTSIDE_CAP)

#drawing the cap of the top part of the S
sparty.right(90)
sparty.forward(CAP_WIDTH)

#draw up to the inside of the S
sparty.right(90)
sparty.forward(INSIDE_CAP)

#head back towards the middle
sparty.left(90)
sparty.forward(SMALL_INSIDE_WIDTH)

#draw down the inside of the top of the S
sparty.left(90)
sparty.forward(INSIDE_VERTICAL)

#draw the top the middle of the S
sparty.left(90)
sparty.forward(LARGE_INSIDE_WIDTH)

#angle down
sparty.right(45)
sparty.forward(DIAG)

#draw the outside right vertical line
sparty.right(45)
sparty.forward(OUTSIDE_VERTICAL)

#bottom right diag
sparty.right(45)
sparty.forward(DIAG)

#bottom of S
sparty.right(45)
sparty.forward(OUTSIDE_WIDTH)

#bottom left diag
sparty.right(45)
sparty.forward(DIAG)

#the bottom cap of the S
sparty.right(45)
sparty.forward(OUTSIDE_CAP)
sparty.right(90)
sparty.forward(CAP_WIDTH)
sparty.right(90)
sparty.forward(INSIDE_CAP)

#The smaller bottom inside
sparty.left(90)
sparty.forward(SMALL_INSIDE_WIDTH)

#draw up the inside of the bottom of the S
sparty.left(90)
sparty.forward(INSIDE_VERTICAL)

#And draw the larger middle
sparty.left(90)
sparty.forward(LARGE_INSIDE_WIDTH)

#diag up
sparty.right(45)
sparty.forward(DIAG)

#one last up on the left side
sparty.right(45)
sparty.forward(OUTSIDE_VERTICAL)

#and one last diag to bring us back to the beginning.
sparty.right(45)
sparty.forward(DIAG)


#waiting for user input to end the program
input()



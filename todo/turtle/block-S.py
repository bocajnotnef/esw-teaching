#! /usr/bin/env python3

"""
Draws a block S 
"""

#import the turtle module 
#and be able to use the commands 
import turtle 

#common widths for the block S 
DIAG=75

#make the "turtle object" 
#this is our "turtle" that will
#run around the screen 
sparty = turtle.Turtle()

#set the color to be THE spartan green 
sparty.pencolor("#18453B") 

#Put the pen "up" so that when we move we dont draw
sparty.penup()

#Set the pen width 
sparty.width(20)

#move sparty to the top left since that's where were starting 
sparty.setx(-200)
sparty.sety(200)

#put the pen "down" so that we can start drawing
sparty.pendown()

#Draw the top part of the block S 
sparty.forward(300)

#right 45 degrees and draw the next part 
sparty.right(45)
sparty.forward(DIAG)

#drawing down
sparty.right(45)
sparty.forward(100)

#drawing left 
sparty.right(90)
sparty.forward(100)

#draw up from the edge of the S
sparty.right(90)
sparty.forward(50)

#angle back 
sparty.left(90)
sparty.forward(200)

#draw down the inside of the top of the S
sparty.left(90)
sparty.forward(100)


#draw the middle of the S
sparty.left(90)
sparty.forward(250)

#angle down 
sparty.right(45)
sparty.forward(DIAG)

#angle down again 
sparty.right(45)
sparty.forward(100)

sparty.right(45)
sparty.forward(DIAG)





#waiting for user input to end the program
input()



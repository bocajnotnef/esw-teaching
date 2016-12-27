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

#make the "turtle object"
#this is our "turtle" that will
#run around the screen
sparty = turtle.Turtle()

#the points that sparty will travel to in order 
#to make the block S
points=[
        (-200.00,250.00), (100.00,250.00), (153.03,196.97), (153.03,96.97), 
        (53.03,96.97), (53.03,146.97), (-146.97,146.97), (-146.97,21.97), 
        (103.03,21.97), (156.07,-31.07), (156.07,-256.07), (103.03,-309.10), 
        (-196.97,-309.10), (-250.00,-256.07), (-250.00,-156.07), (-150.00,-156.07), 
        (-150.00,-206.07), (50.00,-206.07), (50.00,-81.07), (-200.00,-81.07), 
        (-253.03,-28.03), (-253.03,196.97), (-200.00,250.00)
        ]

#set the color to be THE spartan green
sparty.pencolor("#18453B")

#Put the pen "up" so that when we move we dont draw
sparty.penup()

#move sparty to starting point of the block S
sparty.goto(points[0]) 

#set the pen down and set the width 
sparty.pendown()
sparty.width(30)

for coord in points:
    sparty.goto(coord)

print("Press enter to end program.")

#waiting for user input to end the program
input()

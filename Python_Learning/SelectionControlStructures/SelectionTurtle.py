'''
Created on 07-May-2020

@author: raghuveer
'''

import turtle

wn = turtle.Screen() # creates a graphics window
wn.setup(540,508)  # set window dimension
alex = turtle.Turtle() # create a turtle named alex
alex.shape("turtle") # alex looks like a turtle
alex.color("red")  # alex has a color

#Write the logic to take the turtle to its destination
#Refer the statements given above to draw the pattern
def turtle_travel(direction):
    if (direction == "south"):
        alex.right(90)
        alex.forward(250)
    elif (direction == "north"):
        alex.left(90)
        alex.forward(250)
    elif (direction == "west"):
        alex.right(180)
        alex.forward(265)
    elif (direction == "east"):  
        alex.forward(265)
    else:
        alex.write("Looks like you have typed a wrong destination")
    return

#Provide different values and test your program
destination="north"

turtle_travel(destination)
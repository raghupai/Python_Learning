'''
Created on 07-May-2020

@author: raghuveer
'''

import turtle # allows us to use the turtles library

wn = turtle.Screen() # creates a graphics window
wn.setup(400,400) # set window dimension

circle_rad=60 # set the radius
rectangle_width= 4 * circle_rad #set the width
rectangle_height= circle_rad / 2 #set the height

alex = turtle.Turtle() # create a turtle named alex
alex.shape("turtle") # alex looks like a turtle
alex.color('red') # alex has a color
alex.circle(circle_rad)
alex.backward(rectangle_width/2)
alex.forward(rectangle_width)
alex.right(90)
alex.forward(rectangle_height)
alex.right(90)
alex.forward(rectangle_width)
alex.right(90)
alex.forward(rectangle_height)
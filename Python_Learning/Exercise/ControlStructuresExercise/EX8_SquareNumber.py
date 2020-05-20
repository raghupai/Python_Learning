'''
Created on 16-May-2020

Write a python function, find_square() that accepts an integer number, n and returns the square of n. 
Invoke the function and display the square of the number. 

@author: raghuveer
'''

def find_square(number):
    return number * number

number = float(input("Enter a number:"))

print("Square of the number is " + str(find_square(number)))
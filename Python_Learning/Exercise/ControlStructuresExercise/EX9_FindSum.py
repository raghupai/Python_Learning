'''
Created on 16-May-2020

Write a python function, find_sum() that accepts an integer, n and returns the sum of first, n numbers. 
Invoke the function and display the sum of first n numbers.

@author: raghuveer
'''

def find_sum(number):
    return int(number * (number+1) / 2)

number = int(input("Enter a number:"))

print("Sum of numbers till " + str(number)+" is "+str(find_sum(number)))
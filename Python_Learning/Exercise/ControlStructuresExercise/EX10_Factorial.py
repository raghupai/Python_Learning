'''
Created on 16-May-2020

Write a Python function factorial(num) which returns the factorial of a given number.

@author: raghuveer
'''

def factorial(num):
    Total = 1
    if (num == 0 or num == 1):
        return Total
    else:
        return num * factorial(num-1)
    
number = int(input("Enter a number:"))

print("Factorial of "+str(number)+" is "+str(factorial(number)))
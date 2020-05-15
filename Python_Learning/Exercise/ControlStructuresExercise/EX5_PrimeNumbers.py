'''
Created on 15-May-2020

Write a Python program to check the given number is prime number or not.

@author: raghuveer
'''

from math import sqrt

def prime_number(num):
    flag = 0
    for i in range(2, int(sqrt(num))):
        if (num % i == 0):
            flag = 1
            break
    
    return flag

num = int(input("Enter a number:"))

if(prime_number(num) == 1):
    print("Number is not a prime")
else:
    print("Number is a prime")


        
    
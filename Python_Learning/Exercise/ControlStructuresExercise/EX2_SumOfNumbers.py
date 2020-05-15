'''
Created on 10-May-2020

Write a Python program to find the sum of digits of a given number.

Example: Sum of number 123 will be 6

Note: Initialize the number with various values and test your program.

@author: raghuveer
'''

def sum_of_digits(number):
    Total = 0
    while (number > 0):
        Total += (number % 10)
        number = int(number / 10)
    return Total

num = input("Enter a number :")

num = int(num)

result = sum_of_digits(num)

print(result)

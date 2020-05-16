'''
Created on 15-May-2020

Write a Python program to print first n Fibonacci numbers.

@author: raghuveer
'''

def fibonacci(num):
    f0 = 0
    f1 = 1
    temp = 0
    fib_list = []
    if num == 1:
        fib_list.append(f0)
    elif num == 2:
        fib_list.append(f0)
        fib_list.append(f1)
    else:
        fib_list.append(f0)
        fib_list.append(f1)
        while (num > 2):
            fib_list.append(f0+f1)
            num -= 1
            temp = f0 + f1
            f0 = f1
            f1 = temp
    return fib_list

num = int(input("Input a number:"))

print(fibonacci(num))


'''
Created on 16-May-2020

Write a Python Function is_palindrome(num) that accepts an integer num as argument and returns True if the num is palindrome else returns false. 
Invoke the function and based on return value print the output.

@author: raghuveer
'''

def is_palindrome(num):
    temp_lst = []
    flag = 0
    while (num > 0):
        temp_lst.append(num % 10)
        num = int(num/10)
    
    for i in temp_lst:
        if (i == temp_lst[len(temp_lst) - 1]):
            flag = 1
  
    return flag   
    
#number = int(input("Enter a number:"))

if (is_palindrome(122) > 0):
    print("Number is a palindrome")
else:
     print("Number is not a palindrome")
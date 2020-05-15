'''
Created on 10-May-2020

Write a Python program to find and display the maximum of three given numbers.

@author: raghuveer
'''

def max_numbers(nums_list):
    if(nums_list[0] > nums_list[1]):
        if(nums_list[0] > nums_list[2]):
            return nums_list[0]
        else:
            return nums_list[2]
    else:
        if(nums_list[1] > nums_list[2]):
            return nums_list[1]
        else:
            return nums_list[2]
    
print(max_numbers([4,6,3]))
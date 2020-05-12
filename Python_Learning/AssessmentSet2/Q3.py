'''
Created on 12-May-2020

@author: raghuveer
'''

name1 ="Roger"
name2 = "Robert"

def swap_names(name1, name2):
    temp = name1
    name1 = name2
    name2 = temp

print("Before Swapping: name1 = "+name1+" name2 = "+name2)
swap_names(name1, name2)
print("After Swapping: name1 = "+name1+" name2 = "+name2)
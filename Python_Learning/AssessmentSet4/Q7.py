'''
Created on 15-May-2020

@author: raghuveer
'''

def func(my_lst, var1):
    new_lst = []
    for num in my_lst:
        if (num % var1 == 0):
            new_lst.append(num//var1)
        else:
            new_lst.append(0)
    return new_lst

my_lst = [13,17,23,27,33,37]
var1 = 7

print(func(my_lst, var1))
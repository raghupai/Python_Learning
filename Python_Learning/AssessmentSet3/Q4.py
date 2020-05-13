'''
Created on 13-May-2020

@author: raghuveer
'''

def remove_odd(list1):
    for index in range(len(list1)):
        if list1[index] %2 == 0:
            list1.remove(list1[index])

list1=[1, 2, 3, 4, 5]
remove_odd(list1)
print(list1)
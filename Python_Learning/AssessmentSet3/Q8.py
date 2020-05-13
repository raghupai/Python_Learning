'''
Created on 13-May-2020

@author: raghuveer
'''

def move(list1, list2):
    for num in list1:
        list2.append(num)
        list1.remove(num)
        
list1 = [1, 2, 3, 4, 5]
list2 = [10]
move(list1, list2)
print((list1, list2))
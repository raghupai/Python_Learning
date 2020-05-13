'''
Created on 13-May-2020

@author: raghuveer
'''

def average(list1):
    sum, count = 0, 0
    for index in range(0, len(list1) - 1):
        sum += list1[index]
        count += 1
    return sum/count
print(average([1, 2, 3, 4, 5]))
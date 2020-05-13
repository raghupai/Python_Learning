'''
Created on 13-May-2020

@author: raghuveer
'''
import math

num_list = [32.5,44.2, 66.6, 78.4, 99.2]

for num in range(0, len(num_list)):
    num_list[num]=math.ceil(num_list[num])

num_list.reverse()
print(num_list)
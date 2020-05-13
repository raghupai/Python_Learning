'''
Created on 13-May-2020

@author: raghuveer
'''

result = 0
list1 = [10, 20, 30]
list2 = [1,2]

for num in range(len(list1)):
    for num in range(len(list2)):
        result += list1[num] + list2[num]

print(result)
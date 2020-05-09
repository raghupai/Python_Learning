'''
Created on 07-May-2020

@author: raghuveer
'''

num_list = [1,33,31,5,26,7,8,92,10]
num = 10
flag = 0
count = 0
for item in num_list:
    if(item == num):
        flag = 1
        count += 1
        break
    else:
        count += 1
        continue
if(flag == 1):
    print(num, "found in the list after", count ," comparisons")
else:
    print(num, "NOT found in the list")
'''
Created on 12-May-2020

@author: raghuveer
'''

my_str = "All3 that4 glitters8 is2 not3 gold4"
my_list = []

'''
for char in my_str:
    if(char.isdigit()):
        my_list.append((int)(char))
        my_str = my_str.replace(char, "")

print(my_str, my_list)
'''

for char in my_str:
    if(char.isdigit()):
        my_list.append(char)
        my_str.replace(char, "")

print(my_str, my_list)
'''
Created on 12-May-2020

@author: raghuveer
'''

#lex_auth_01269437118923571233

def factorial(number):
    fact = 1
    if (number == 0):
        return fact
    else:
        while (number > 0):
            fact = fact * number
            number -= 1
        return fact

def find_strong_numbers(num_list):
    temp_list = []
    flag = 0
    for i in num_list:
        sum = 0
        if (i == 0):
            sum = 1
        while (i > 0):
            sum = sum + factorial(i % 10)
            i = int(i / 10)
        if (sum == num_list[flag]):
            temp_list.append(sum)
        flag += 1    
    return temp_list

num_list=[145, 375, 100, 2, 10, 40585, 0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
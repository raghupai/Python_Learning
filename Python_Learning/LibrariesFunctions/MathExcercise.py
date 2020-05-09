'''
Created on 10-May-2020

@author: raghuveer
'''

#lex_auth_01269437590597632045

import math

def find_number_of_combination(number_of_flavours):
    total_combination=0
    #write your logic here
    for i in range(0,number_of_flavours+1):
        temp = math.factorial(number_of_flavours)/(math.factorial(i) * (math.factorial(number_of_flavours - i)))
        total_combination = total_combination + temp
    return total_combination


#Provide different values for number_of_flavours and test your program
number_of_combination=find_number_of_combination(4)
print(number_of_combination)
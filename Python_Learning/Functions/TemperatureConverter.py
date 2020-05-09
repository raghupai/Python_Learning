'''
Created on 07-May-2020

@author: raghuveer
'''

def temperature_converter(degree_F):
    #All the statements in the block of code must have the same level of indentation
    degree_C = (((degree_F - 32) * 5) / 9)
    return degree_C

result=temperature_converter(100)
print(result)
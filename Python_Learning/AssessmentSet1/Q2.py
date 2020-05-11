'''
Created on 11-May-2020

@author: raghuveer
'''

def modify_list(arg_list):
    arg_list=arg_list + [60, 70, 80]
    print("Inside function:", arg_list)
    
i_list=[10,20,30,40,50]
print("Before function call:", i_list)
modify_list(i_list)
print("After function call:", i_list)
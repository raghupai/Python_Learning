'''
Created on 15-May-2020

Write a python function, find_pairs_of_numbers() which accepts a list of positive integers with no repetitions 
and returns count of pairs of numbers in the list that adds up to n. 
The function should return 0, if no such pairs are found in the list.
@author: raghuveer
'''

#lex_auth_01269438594930278448

def find_pairs_of_numbers(num_list,n):
    count = 0
    for i in range(0,len(num_list)):
        for j in range(1, len(num_list)):
            if (num_list[i] + num_list[j] == n)
    #Remove pass and write your logic here

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))
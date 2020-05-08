#lex_auth_01269441913243238467
from audioop import reverse
from _ast import Num

def create_largest_number(number_list):
    number_list.sort()
    temp = 0
    for i in range(0, len(number_list)):
        temp += number_list[i] * (10 ** (2 * i))

        
    return temp


number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
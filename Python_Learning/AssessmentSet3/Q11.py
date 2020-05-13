'''
Created on 13-May-2020

@author: raghuveer
'''

total = 0
try:
    try:
        num_list=[1, 2, 0, 0]
        for num in range(len(num_list)):
            total += (num_list[num] - num_list[num-1])*4 // (num_list[num]+num_list[num+1])
    except ZeroDivisionError:
        print("ZD", end=" ")
    except:
        print("Other", end=" ")
    finally:
        print("FI", end=" ")
    print(total)
except IndexError:
    print("IN")
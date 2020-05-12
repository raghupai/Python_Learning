'''
Created on 12-May-2020

@author: raghuveer
'''

def func(sample, res, key, val):
    if (key in sample):
        res = True
        sample.update({key:val})
    res = False

res = None
sample = {"XS":1, "X":0, "XL":3, "XXL":4}
func(sample, res, "X", 2)
print(sample["X"], res)
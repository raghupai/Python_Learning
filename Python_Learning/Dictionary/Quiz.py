'''
Created on 09-May-2020

@author: raghuveer
'''

sample_dict = {'a':1,'b':2}
sample_dict.update({'b':5, 'c':10 })
print(sample_dict.get('b'), sample_dict.get('c'))
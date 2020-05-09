'''
Created on 10-May-2020

@author: raghuveer
'''
import re
word="New Airlines4"
if(re.search(r"^N",word) and re.search(r"e$",word)):
    print(re.sub(r"New",r"Old",word))
else:
    print(re.sub(r"s(\d{1})",r"S\1",word))
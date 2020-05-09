'''
Created on 10-May-2020

@author: raghuveer
'''

import re

#. - Used to match one occurrence of any character
if(re.search(r"A..l","Aopline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
#\d - Used to match one occurrence of any digit from 0-9
if(re.search(r"A\dl","A2line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

#* - Used to match one or more occurrences of previous character
if(re.search(r"A\d*","A2234line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
#+ - Used to match one or more occurrences of previous character
if(re.search(r"A\d+","A2irline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
#? - Used to match zero or one occurrence of previous character
if(re.search(r"A\d?i","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

#{n} - Used to match exactly n occurrences of previous character
if(re.search(r"A\d{3}i","A223irline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
#[] - Used to match one occurrence of any characters present within square brackets
if(re.search(r"A[4-8]l","A7line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
#^ - Used to match a pattern at the beginning of a string
if(re.search(r"^A","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

#$ - Used to match a pattern at the end of a string
if(re.search(r"e$","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
#\w - Used to match an word character which includes alphabets(a-zA-Z), digits(0-9) and '_'
if(re.search(r"\w$","Airlines")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
#\s - Used to match single space or sequence of spaces (including \t \n)
if(re.search(r"Air\s","Air line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

#| - Used to match any one pattern which is on either side of it
if(re.search(r"Hell|Fell","Fellow")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
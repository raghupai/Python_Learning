'''
Created on 12-May-2020

@author: raghuveer
'''

marks = ["FA1", 80, "FA2", 85, "FA3", 95]
report = marks[-4:]
report=report[:1]+marks[5:]
print(report)
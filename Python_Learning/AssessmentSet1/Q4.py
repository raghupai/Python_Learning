'''
Created on 11-May-2020

@author: raghuveer
'''

FHW=open("data.txt","w")
FHW.write("written some thing")
print(FHW.tell())
print("closed?",FHW.closed)
FHW.close()
print("after closing the file closed?",FHW.closed)
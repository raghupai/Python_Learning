'''
Created on 13-May-2020

@author: raghuveer
'''

def tower_of_hanoi(n, source,destination,temp):
    if(n==1):
        disk=source.pop(0) #Removes the element in specified position
        destination.insert(0,disk) #Inserts the given element in specified position
        return
    tower_of_hanoi(n-1, source, temp, destination)
    disk=source.pop(0)
    destination.insert(0,disk)
    tower_of_hanoi(n-1, temp, destination, source)
    return

source=[3,2,1,4]
destination=[]
temp=[]
tower_of_hanoi(len(source), source, destination, temp)
print("Source:",source)
print("Destination:",destination)
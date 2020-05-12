'''
Created on 12-May-2020

@author: raghuveer
'''

temp = "Hello? how are you?"
if(temp.isdigit()):
    temp += "fine"
else:
    for var1 in range(len(temp)):
        if(temp[var1] == '?'):
            final_val=temp[:var1]
            break

if(final_val.endswith('u')):
    final_val = final_val.replace('you', 'u')
else:
    final_val = final_val.upper()
    
print(final_val)
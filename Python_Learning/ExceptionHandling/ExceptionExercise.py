'''
Created on 13-May-2020

@author: raghuveer
'''

#lex_auth_01269437504257228837

def find_average(mark_list):
    total=0
    marks_avg = 0
    try:
        for i in range(0, len(mark_list)):
            total+=mark_list[i]
            marks_avg=total/len(mark_list)
    except NameError:
        print("Name Error Occured")
    except ValueError:
        print("Value Error Occured")
    except TypeError:
        print("Type Error Occured")
    except ZeroDivisionError:
        print("Zero Division Error Occured")
    except:
        print("Some Error Occured")
    return marks_avg
    
try:
    m_list=[]
    print("Average marks:", find_average(m_list))
except NameError:
    print("Name Error Occured")
except ValueError:
    print("Value Error Occured")
except TypeError:
    print("Type Error Occured")
except ZeroDivisionError:
    print("Zero Division Error Occured")
except:
    print("Some Error Occured")
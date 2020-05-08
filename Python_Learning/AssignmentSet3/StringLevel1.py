'''
Created on 08-May-2020

@author: raghuveer
'''
#lex_auth_012693819159732224162

def check_palindrome(word):
    word.upper()
    temp_word = word[::-1]
    
    if (temp_word == word):
        return True
    else:
        return False
    


status=check_palindrome("malyalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
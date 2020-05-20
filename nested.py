# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

char=input()
if ord(char)>=65 and ord(char)<=90:
    print('Upper case alphabet')
    if char in ['A','E','I','O','U']:
        print('Vowel uppercase')
    else:
        print('consonant')

elif ord(char)>=97 and ord(char)<=122:
    print('Lower case alphabet')
    if char in ['a','e','i','o','u']:
        print("Vowel")
    else:
        print('Consonant')
else:
    print('Good Bye')
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:00:42 2020

@author: lenovo
"""


count=0
print("Enter your name")
name=input()
for letter in name:
    if (letter in['a','e','i','o','u','A','E','I','O','U']):
        count +=1
print(count)

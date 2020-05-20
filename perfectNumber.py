# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:05:48 2020

@author: lenovo
"""


def perfect_number(num):
    count=0
    for i in range(1,num):
        if num%i==0:
            count+=i
    if num==count:
        print('perfect number')
    else:
        print('Not perfect')
def main():
    x=int(input("enter number"))
    print()
    p=perfect_number(x)
    
if __name__=='__main__':
    main()
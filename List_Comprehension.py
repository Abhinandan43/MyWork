# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:26:45 2020

@author: Abhinandan
"""
x=int(input())
y=int(input())
z=int(input())
n=int(input())
print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k !=n])


'''
input format :
 x=1
 y=1
 z=1
 n=2
 
 Output format:
 [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

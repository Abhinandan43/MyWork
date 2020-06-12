# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:41:09 2020

@author: Abhinandan
"""

def reversing_sentance(sentance):
    words=sentance.split(' ')
    reversed_word=' '.join(reversed(words))
    return reversed_word.swapcase()
def main():
    x=input()
    y=reversing_sentance(x)
    print(y)
if __name__=='__main__':
    main()
    
    
    
    '''
      input: aWESOME is cODING
      Output: Coding IS Awesome

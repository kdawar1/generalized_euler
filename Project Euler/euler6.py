# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:12:51 2020

@author: kshit
"""


'''
The sum of the first N natural numbers is expressed as
    S_n = (n)(n+1)/2
The sum of the squares of the first N natural numbers is expressed as
    S_squared_n = (n)(+1)(2n+1)/6
Hence this would drastically speed up the process of finding the difference of squares
'''

def diff_sq(num):
    #num is the maximum number of natural numbers
    
    S_n = num * (num + 1) / 2
    S_squared_n = num * (num + 1) * (2 * num + 1) / 6
    
    return S_n * S_n - S_squared_n
    
if __name__ == '__main__':
    print(diff_sq(100))
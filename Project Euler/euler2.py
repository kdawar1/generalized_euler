# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:45:21 2020

@author: kshit
"""


def fib_sum_even(i):
    a = 1
    b = 2
    sum_fib = 0
    while b < i:
        if b % 2 == 0:
            sum_fib += b
        
        a , b = b, a + b
    
    return sum_fib

if __name__ == "__main__":
    print(fib_sum_even(4000000))


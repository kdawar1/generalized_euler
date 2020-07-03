# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:39:48 2020

@author: kshit
"""
import math

def sum_factorial(number):
    factorial = str(math.factorial(number))
    sum_digits = sum(int(i) for i in factorial)
    return sum_digits

if __name__ == '__main__':
    print(sum_factorial(100))
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:39:40 2020

@author: kshit
"""

def euler_1(num):
    get_sum = sum(x for x in range(num) if (x % 3 == 0 or x % 5 == 0))
    return get_sum

if __name__ == "__main__":
    print(euler_1(1000))
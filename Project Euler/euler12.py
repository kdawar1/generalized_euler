# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:27:59 2020

@author: kshit
"""
import math
import itertools

# find divisors
def find_divisors(n):
    count_divisors = 0
    end = math.floor(math.sqrt(n))
    for i in range(1, end + 1):
        if n % i == 0:
            count_divisors += 2
    if end**2 == n:
        count_divisors += -1
    return count_divisors
# find num of divisors

triangle_num = 0
for i in itertools.count(1):
    triangle_num += i
    num_divisors = find_divisors(triangle_num)
    if num_divisors > 500:
        print(triangle_num)
        break
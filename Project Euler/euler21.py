# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:45:56 2020

@author: kshit
"""

# find sum of divisors using Sieve of Eratosthenes
def sum_amicable(upper_limit):
    sum_divisors = [0] * upper_limit
    for i in range(1, upper_limit):
        for j in range(i * 2, upper_limit, i):
            sum_divisors[j] += i
    
    sum_amic = 0

    for i in range(1, upper_limit):
        j = sum_divisors[i]
        if j != i and j < upper_limit and sum_divisors[j] == i:
            sum_amic += i
    return sum_amic

if __name__ == '__main__':
    print(sum_amicable(10000))
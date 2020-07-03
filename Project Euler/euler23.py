# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 17:03:44 2020

@author: kshit
"""


def non_abundant_sums(upper_limit):
    sum_div = [0] * upper_limit
    for i in range(1, upper_limit):
        for j in range(i * 2, upper_limit, i):
            sum_div[j] += i

    abundant = [i for (i, x) in enumerate(sum_div) if x > i]
    
    check = [False] * upper_limit
    
    for i in abundant:
        for j in abundant:
            if i + j < upper_limit:
                check[i+j] = True
            else:
                break
            
    sum_non_ab = sum(i for (i, j) in enumerate(check) if not j)
    return sum_non_ab

if __name__ == '__main__':
    print(non_abundant_sums(28124))
                    
            
    
    
        
        
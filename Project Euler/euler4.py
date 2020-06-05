# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:08:25 2020

@author: kshit
"""

'''
We want to find the largest palindrome formed from the multiple of 2 3 digit numbers (x and y).
The palindrome will be of the form abccba.
(10^5)*a+(10^4)*b+...+(10^0)*a = 100001*a+10010*b+1100*c=11*(9091*a+910*b+100*c)
Hence atleast 1 of x and y has to be multiple of 11.
Hence, we can assume x to be a multiple of 11 and then develop the product of x (starting from 990 down towards 110)
and y (starting from 999 to 100) and check to see if the product is a palindrome.
We store the first palindrome we encounter and keep on checking for other products subsequently.
One way of improving efficiency is to not check for all y s for a given x if the product of x and y is less than the 
palindrome.
'''

def largest_palindrome():
    max_palindrome = 0
    for x in range(990, 110, -11):
        for y in range(999, 100, -1):
            if x*y < max_palindrome:
                continue
            if str(x*y) == str(x*y)[::-1]:
                if x*y > max_palindrome:
                    max_palindrome = x*y
    return max_palindrome

if __name__ == '__main__':
    print(largest_palindrome())

    

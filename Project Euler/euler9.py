# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:56:36 2020

@author: kshit
"""
'''
Pythagorean Triplets can be generated by the formula.

Given any positive integers m and n where m > n > 0, the integers
a = m^2 - n^2
b = 2*m*n
c = m^2 + n^2
'''
def dicksinson_pythagorus():
	for m in range(1,32):
		for n in range(1,m):
			a = m**2 - n**2
			b = 2 * m * n
			c = m**2 + n**2
			if a + b + c == 1000:
				return a*b*c


if __name__ == '__main__':
    print(dicksinson_pythagorus())

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:02:23 2020

@author: kshit
"""

from numpy import arange
from math import gcd

def lcm_array(arr):
	lcm = 1
	for i in arr:
		lcm *= i // gcd(i, lcm)
	return lcm

if __name__ == '__main__':
    print(lcm_array(arange(1,21)))
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:15:13 2020
@author: kshit
"""
import math

def largest_prime(num):
    #Ensure the number is atleast 2
    if num < 2:
        return 'Invalid number'
    #If number is 2, then the largest prime factor is 2
    if num == 2:
        return 2
    
    #Initialize largest prime factor to -1
    max_prime_factor = -1
    
    #Divide number by 2 until the number is no longer even. This avoids the need to check for even multiples
    while num % 2 == 0:
        num /= 2
    
    #We need to check for odd numbers from 3 until upper bound rounding of square root of num
    for i in range(3, round(math.sqrt(num)) + 1, 2):
        while num % i == 0: #checking if the number divides num. If so, set the number as the highest multiple of num
            max_prime_factor = i
            num /= i
            
    if num > 1:
        return num #If the remainder isn't 1, then it implies that the largest divisor is the remaining num
        
    return int(max_prime_factor)

if __name__ == '__main__':
    print(largest_prime(600851475143))
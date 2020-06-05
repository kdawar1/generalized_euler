# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:19:05 2020

@author: kshit
"""
'''
There is faster way based upon the AKS primality test.
The AKS primality test is based upon the following theorem: 
Given an integer n>=2 and integer a coprime to n, n is prime if and only if the polynomial congruence relation
(x+a)^n =  (x^n+a)  (mod n)
holds.  Note that x should be understood as a formal symbol.
'''
import eulerlib, itertools

def find_nth_prime_1(num):
	prime = next(itertools.islice(filter(eulerlib.is_prime, itertools.count(2)), num - 1, None))
	return prime

def find_nth_prime_2(num):
    count = 1
    list_primes = []
     
    list_primes.append(2)
     
    while len(list_primes) < num:
        count += 2
        i = 0
        is_prime = True
        while (list_primes[i] * list_primes[i] <= count):
            if count % list_primes[i] == 0:
                is_prime = False
                break
            i += 1
        
        if is_prime:
            list_primes.append(count)
    return list_primes[-1]
    

if __name__ == "__main__":
    print(find_nth_prime_1(10001))
    print(find_nth_prime_2(10001))
    
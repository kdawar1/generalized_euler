# -*- coding: utf-8 -*-
def circular_primes(num):
    prime = [True] * (num+1)
    prime[0] = False
    prime[1] = False
    i = 2
    while (i*i <= num):
        if prime[i] == True:
            for j in range(i*2, num+1, i):
                prime[j] = False
        i += 1
    
    def is_circular_prime(n):
       	s = str(n)
       	return all(prime[int(s[i : ] + s[ : i])] for i in range(len(s)))
    
    ans = sum(1 for i in range(len(prime))if is_circular_prime(i))
    return ans
    
if __name__ == '__main__':
    print(circular_primes(1000000))
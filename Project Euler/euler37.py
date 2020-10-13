# -*- coding: utf-8 -*-
import itertools
def is_prime(num) : 
  
    if (num <= 1) : 
        return False
    if (num <= 3) : 
        return True
  
    if (num % 2 == 0 or num % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= num) : 
        if (num % i == 0 or num % (i + 2) == 0) : 
            return False
        i = i + 6
        
    return True


def is_truncatable_prime(n):
	i = 10
	while i <= n:
		if not is_prime(n % i):
			return False
		i *= 10
	
	while n > 0:
		if not is_prime(n):
			return False
		n //= 10
	return True

def sum_truncatable_primes(num_primes):
	ans = sum(itertools.islice(filter(is_truncatable_prime, itertools.count(10)), num_primes))
	return str(ans)

if __name__ == '__main__':
    print(sum_truncatable_primes(11))


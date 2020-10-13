# 9!*7 is the upper limit as 9! * 8 is 7 digit number
import numpy as np

def factorial(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

list_num = np.arange(10)
list_fact = [factorial(i) for i in list_num]

def factorial_digits(n):
	s = 0
	while n:
		s += list_fact[n%10]
		n //= 10
	return s

def fact_digit_sums():
    solution = 0

    for i in range(10,list_fact[-1]*7):
        if factorial_digits(i) == i:
            solution += i

    return solution
 
if __name__ == '__main__':
    print(fact_digit_sums())
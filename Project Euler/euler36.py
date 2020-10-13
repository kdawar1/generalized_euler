# -*- coding: utf-8 -*-

def palindrome(num):
	s = str(num)
	if s != s[ : : -1]:
		return False
	t = bin(num)[2 : ]
	return t == t[ : : -1]

def sum_pal(limit):
	return sum(i for i in range(limit) if palindrome(i))

if __name__ == '__main__':
    print(sum_pal(1000000))

# Using the seive of Eratosthenes https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def sum_primes(n):
    sum = 0
    sieve = [True] * n
    for i in range(2, n):
        if sieve[i]:
            sum += i
            for j in range(i**2, n, i):
                sieve[j] = False
    return sum

if __name__ == "__main__":
	print(sum_primes(2000000))
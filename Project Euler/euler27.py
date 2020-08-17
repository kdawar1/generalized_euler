# x = n^2 + an + b; |a| < 1000 and |b| < 1000 
# b has to be odd, positive and prime as we are testing consecutive values for n
# a has to be negative otherwise the difference between consecutive x's will be huge!
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

def max_prod(max_val_a , max_val_b):
    max_n = 0   
    max_b = 0   
    max_a = 0   
    for i in range(-max_val_a, -1):
        for j in range(1, max_val_b, 2):
            n = 0
            while is_prime(n**2 + i*n + j):
                n += 1
            if n > max_n:
                max_a = i
                max_b = j
                max_n = n
    return max_a * max_b


if __name__ == '__main__':
    print(max_prod(1000, 1000))
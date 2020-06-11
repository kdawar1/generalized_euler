def memoize(f): 
    memo = {} 
  
    def inner(num): 
        if num not in memo:          
            memo[num] = f(num) 
        return memo[num] 
  
    return inner 

@memoize
def collatz_length(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        y = x // 2
    else:
        y = 3 * x + 1
    return collatz_length(y) + 1

def find_longest(max_limit):
    max_num = max(range(1, max_limit), key=collatz_length)
    return max_num

if __name__ == "__main__":
    print(find_longest(1000000))

def power_sum(num_digits):
    sum_pow = 0
    for i in range(2, (num_digits+1)*(9**num_digits)):
        sum_digits = sum(a**num_digits for a in get_digits(i))
        if i == int(sum_digits):
            sum_pow += i
    return sum_pow

def get_digits(num):
    ans = []
    while num > 0:
        ans.append(num%10)
        num = num//10
    return ans

if __name__ == '__main__':
    print(power_sum(5))
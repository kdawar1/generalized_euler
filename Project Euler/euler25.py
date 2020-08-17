def first_fib_digits(digits):
    x = 1
    y = 1
    count = 2
    while len(str(y)) < digits:
        count = count + 1
        x, y = y, x + y
    return count

if __name__ == '__main__':
    print(first_fib_digits(1000))
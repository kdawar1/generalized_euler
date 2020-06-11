def sum_digits(num, pow):
    return sum(int(i) for i in str(num ** pow))

if __name__ == "__main__":
    print(sum_digits(2, 1000))

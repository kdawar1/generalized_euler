def distinct_pow(a_min, a_max, b_min, b_max):
    prod = set(a**b for a in range(a_min, a_max+1) for b in range(b_min, b_max+1))
    return len(prod)

if __name__ == '__main__':
    print(distinct_pow(2,100,2,100))
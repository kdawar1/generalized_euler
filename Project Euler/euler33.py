import numpy as np
def digit_cancel(num_digit):
    fin_num = 1
    fin_den = 1
    for den in range(10**(num_digit-1),10**(num_digit)):
        for num in range(10**(num_digit-1),den):
            n_units = num % 10
            n_tens = num // 10
            d_units = den % 10
            d_tens = den // 10
            if (n_tens == d_units and n_units * den == num * d_tens) or (n_units == d_tens and n_tens * den == num * d_units):
                fin_num *= num
                fin_den *= den
    return (fin_den // np.gcd(fin_num,fin_den))
if __name__ == '__main__':
    print(digit_cancel(2))
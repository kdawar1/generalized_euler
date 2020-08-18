# analytical solution
# Let n be the ring number and f(n) denote the sum of the diagonals, then
# f(0)= 1 and f(1)=1+3+5+7+9=25 .....
# sum of corners for a ring is 4(2n+1)^2 -12n
# hence, f(n) = 4(2n+1)^2 -12n + f(n-1) = ax^3+bx^2+cx+d
# f(0)=d=1
# f(1)=a+b+c+d=25
# f(2)=8a+4b+2c+d=101
# f(3)=27a+9b+3c+d=261
# a=16/3, b=10, c=26/3, d=1
def spiral_diag(square_dim):
    ans_sum = 1
    i = 1
    add = 2
    count = 1
    while i < square_dim**2:
        i = i + add
        ans_sum +=i 
        count = count + 1
        if count == 5:
            add += 2
            count = 1
    return ans_sum

def analytical_soln(square_dim):
    x = (square_dim - 1)/ 2
    return int(16/3*(x**3)+10*(x**2)+26/3*x+1)

if __name__ == '__main__':
    print(spiral_diag(1001))
    print(analytical_soln(1001))
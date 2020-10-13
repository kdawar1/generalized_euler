# -*- coding: utf-8 -*-

def pyth_perimeter(limit):
    ans = 0
    solutions = 0
    for i in range(2,limit+1,2):
        num_sol = 0
        for j in range(2, i//3 + 1):
            if i*(i-2*j) % (2*(i-j)) == 0:
                num_sol +=1
        if num_sol > solutions:
            solutions = num_sol
            ans = i
            
    return ans

if __name__ == "__main__":
	print(pyth_perimeter(1000))
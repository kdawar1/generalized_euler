from scipy.special import factorial

def move_combinations(x_dim, y_dim):

    num_comb = factorial(x_dim+y_dim)/(factorial(x_dim)*factorial(y_dim))
    return int(num_comb)

if __name__ == "__main__":
    print(move_combinations(20,20))
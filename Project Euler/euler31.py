AVAIL_COINS = [1, 2, 5, 10, 20, 50, 100, 200]
# please enter coin required in pence
def coin_combinations(den):
    comb = [1] + [0] * den
    for coin in AVAIL_COINS:
        for i in range(len(comb) - coin):
            comb[i+coin] += comb[i]
    return comb[-1]
if __name__ == '__main__':
    print(coin_combinations(200))
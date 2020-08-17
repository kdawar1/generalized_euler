from itertools import permutations, islice
from numpy import arange
def lexi(arr, num):
    temp = islice(permutations(arr), num-1, None)
    return "".join(str(x) for x in next(temp))


if __name__ == '__main__':
    print(lexi(arange(10),10**6))
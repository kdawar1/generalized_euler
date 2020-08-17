import itertools

def cycle_len(num): 
  a = 1
  b = {}
  for i in itertools.count():
    if a in b:
        return i - b[a]
    else:
        b[a] = i
        a = a * 10 % num

def max_rep(num):
    rep = max(range(1,num), key = cycle_len)
    return rep


if __name__ == '__main__':
    print(max_rep(1000))
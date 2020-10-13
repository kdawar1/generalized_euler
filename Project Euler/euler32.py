# only check cases where the sum of the digits actually equals 9.

def pandigital():
    pan = set()
    check_set = set('123456789')

    for i in range(9):
        for j in range(999,9999):
            s = str(i)+str(j)+str(i*j)
            if len(s) == 9 and set(s) == check_set:
                pan.add(i*j)
            elif len(s) > 9:
                break

    for i in range(9,99):
        for j in range(99,999):
            s = str(i)+str(j)+str(i*j)
            if len(s) == 9 and set(s) == check_set:
                pan.add(i*j)
            elif len(s)>9: 
                break

    return sum(pan)

if __name__ == '__main__':
    print(pandigital())
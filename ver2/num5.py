for i in range(100):
    n = bin(i)[2:]
    v = n[-3:]
    if i % 3 == 0:
        n = n + v
        print(int(n, 2))
    else:
        n = n + bin(((i % 3) - 1) * 3)[2:]
        print(int(n, 2))
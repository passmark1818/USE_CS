for i in range(1000, 10000):
    f1 = i // 1000
    f = i // 100 % 10
    s = i // 10 % 10
    t = i % 10
    m = max(f, s, t, f1)
    n = min(f, s, t, f1)
    k = f + s + t + f1
    p1 = k - m
    p2 = k - n
    ans = str(p1) + str(p2)
    if ans == '1318':
        print(i, ans)
        break

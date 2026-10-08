for i in range(1000, 10000):
    f = i // 1000
    s = i // 100 % 10
    t = i // 10 % 10
    f1 = i % 10
    
    s1 = f + s + t + f1
    m = max(f, s, t, f1)
    n = min(f, s, t, f1)
    p1 = s1 - m
    p2 = s1 - n
    l = str(p2) + str(p1)
    if l == '2013':
        print(i, l)
        break
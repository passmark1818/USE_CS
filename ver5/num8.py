count = 0
for a in range(1, 6):
    for b in range(6):
        for c in range(6):
            for d in range(6):
                for e in range(6):
                    for f in range(6):
                        w = [a, b, c, d, e, f]
                        if w.count(0) == 1:
                            v = True
                            for i in range(6):
                                if w[i] == 0:
                                    if i > 0 and w[i - 1] % 2 != 0:
                                        v = False
                                    if i < 5 and w[i + 1] % 2 != 0:
                                        v = False
                            if v:
                                count += 1
print(count)                                
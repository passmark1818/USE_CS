count = 0
for a in 'aелрст':
    for b in 'aелрст':
        for c in 'aелрст':
            for d in 'aелрст':
                for e in 'aелрст':
                    count += 1
                    w = a + b + c + d + e
                    if a != 'а' and a != 'с' and a != 'т':
                        if w.count('е') == 2 and w.count('ее') == 0:
                            if count % 2 != 0:
                                print(count, w) 
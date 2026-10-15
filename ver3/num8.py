count = 0
for a in 'авкмос':
    for b in 'авкмос':
        for c in 'авкмос':
            for d in 'авкмос':
                for e in 'авкмос':
                    for f in 'авкмос':
                        count += 1 
                        w = a + b + c + d + e + f
                        if a != 'а' and a != 'в' and a != 'к':
                            if w.count('к') == 2 and w.count('кк') == 0:
                                if count % 2 == 0:
                                    print(count)
                                    exit()
                                    
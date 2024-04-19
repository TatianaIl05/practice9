for s in range(1, 10):
    num = [s]
    for e in range(0, 10):
        num.append(e)
        for n in range(0, 10):
            num.append(n)
            for d in range(0, 10):
                num.append(d)
                for m in range(1, 10):
                    num.append(m)
                    for o in range(0, 10):
                        num.append(o)
                        for r in range(0, 10):
                            num.append(r)
                            for y in range(0, 10):
                                num.append(y)
                                if (len(set(num)) == len(num) and s*1000+e*100+n*10+d+m*1000+o*100+r*10+e
                                        == m*10000+o*1000+n*100+e*10+y):
                                    print(f'SEND = {s*1000+e*100+n*10+d}, MORE = '
                                          f'{m*1000+o*100+r*10+e}, MONEY = {m*10000+o*1000+n*100+e*10+y}')
                                num.pop()
                            num.pop()
                        num.pop()
                    num.pop()
                num.pop()
            num.pop()
        num.pop()
    num.pop()

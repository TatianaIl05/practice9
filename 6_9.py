for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a != b != c:
                if (a*10+b)**2 == c*100+a*10+b:
                    print(c*100+a*10+b)

for i in range(100000, 1000000):
    if str(i)[1:] == str(i)[:0:-1]:
        if str(i+1)[1:] == str(i+1)[:0:-1]:
            if str(i+2)[1:5] == str(i+2)[4:0:-1]:
                if str(i+3) == str(i+3)[::-1]:
                    print(i)

n = int(input())

for k in range(2, n+1):
    if n % k == 0:
        print(k)
        break

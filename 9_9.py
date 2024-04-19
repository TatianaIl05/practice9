n = int(input())
dots_sum = 0

for i in range(n+1):
    for j in range(i+1, n+1):
        dots_sum += i+j
    dots_sum += 2*i

print(dots_sum)

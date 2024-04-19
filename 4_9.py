n = int(input())
count = 0

while n != 0:
    n = int(input())
    if n % 4 == 0:
        count += 1

print(count - 1)

def ladder(n, current_floor=1):
    if n == 0:
        return 1

    count = 0
    for i in range(current_floor, n + 1):
        count += ladder(n - i, i + 1)

    return count


result = ladder(int(input()))
print(result)

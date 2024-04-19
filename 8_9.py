number = int(input())

smaller_numbers, checked_numbers = [], []
list_num = 1
count = 0

while list_num**2 < number:
    smaller_numbers.append(list_num**2)
    list_num += 1
for item in smaller_numbers:
    if number - item in checked_numbers:
        count += 1
    checked_numbers.append(item)

print(count)

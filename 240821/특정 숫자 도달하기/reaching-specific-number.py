arr = list(map(int, input().split()))

valid_numbers = []

for num in arr:
    if num >= 250:
        break
    valid_numbers.append(num)

if valid_numbers:
    total_sum = sum(valid_numbers)
    average = total_sum / len(valid_numbers)
else:
    total_sum = sum(arr)
    average = total_sum / len(arr)

print(total_sum, end=" ")
print(average)
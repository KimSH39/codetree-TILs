arr = list(map(float, input().split()))

avg_grade = sum(arr) / len(arr)

print(round(avg_grade, 1))
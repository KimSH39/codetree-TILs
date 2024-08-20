h, w = map(int, input().split())

b = (10000 * w) / (h * h)

print(int(b * 10) // 10)

if b >= 25:
    print("Obesity")
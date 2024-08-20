n, m, o = map(int, input().split())

if n == min(n, m, o):
    print("1", end=" ")
else:
    print("0", end=" ")

if n == m and m == o:
    print("1", end=" ")
else:
    print("0", end=" ")
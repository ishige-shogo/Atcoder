# A問題

a, b = map(int, input().split())

l = a - (2*b)

if l <= 0:
    print(0)
else:
    print(l)

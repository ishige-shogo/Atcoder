
# A問題

s, t = map(str, input().split())
print(t+s)

# B問題

a, b, k = map(int, input().split())

if a >= k:
    print(a-k, b)
elif (a+b) >= k:
    print(0, b-(k-a))
else:
    print(0, 0)

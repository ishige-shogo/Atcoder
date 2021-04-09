# A問題

s, t = map(str, input().split())
a, b = map(int, input().split())
u = input()

if s == u:
    a -= 1
else:
    b -= 1

print(a, b)

# B問題

s = input()
print("x" * len(s))

# C問題

n = int(input())
a = list(map(int, input().split()))

b = set(a)

if len(a) == len(b):
    print("YES")
else:
    print("NO")

# D問題

n, k = map(int, input().split())
p = list(map(int, input().split()))

cnt = sum(p[:k])
m = 0
d = 0

for i in range(n-k):
    d += p[i+k] - p[i]
    m = max(m, d)
ans = cnt + m

print((k+ans)/2)

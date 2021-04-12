# A問題

a = int(input())
b = int(input())

x = [1,2,3]

y = [a, b]

print(list(set(x) - set(y))[0])

# B問題

n = int(input())
s, t = map(str, input().split())

ans = ""

for i in range(n):
    ans += s[i] + t[i]

print(ans)

# C問題
import math
a, b = map(int, input().split())
print(int((a*b)/math.gcd(a, b)))

# D問題
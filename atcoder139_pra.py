# A問題

s = input()
t = input()

ans = 0
for i in range(3):
    if s[i] == t[i]:
        ans += 1

print(ans)


# B問題
import math
a, b = map(int, input().split())
print(math.ceil((b-a)/(a-1))+1)
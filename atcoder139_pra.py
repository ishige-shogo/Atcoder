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

# C問題

n = int(input())
h = list(map(int, input().split()))
cnt, ans = 0, 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)
print(ans)



# A問題

d, t, s = map(int, input().split())

if d > (t * s):
    print("No")
else:
    print("Yes")

#---------------------------------------------------------
# B問題

s = input()
t = input()

m = len(s) - len(t)

ans = len(t)
# T文字列をS文字列に当てはめていき、異なる文字だった場合にカウント
# 一桁ずつずらして検証し、それぞれの最小値を記録していく
for i in range(0, m+1):
    g = i
    count = 0
    for v in range(0, len(t)):
        if s[g]!=t[v]:
            count += 1
        g += 1
    ans = min(ans, count)
print(ans)

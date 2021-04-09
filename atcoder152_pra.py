# A問題

n, m = map(int, input().split())
if n == m:
    print("Yes")
else:
    print("No")

# B問題

n, m = map(int, input().split())
if n >= m:
    print(str(m)*n)
else:
    print(str(n)*m)

# C問題

n = int(input())
p = list(map(int, input().split()))

cnt = max(p)+1
ans = 0
for i in p:
    if cnt >= i:
        ans += 1
    cnt = min(i, cnt)

print(ans)
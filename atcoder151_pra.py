# A問題

c = ord(input())

print(chr(c+1))

# B問題

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

if (n*m - sum(a)) > k:
    print(-1)
elif (n*m - sum(a)) <= 0:
    print(0)
else:
    print(n*m - sum(a))

# C問題

n, m = map(int, input().split())
wa = [0]*n
ac = [0]*n

for _ in range(m):
    p, s = map(str, input().split())
    if ac[int(p)-1]==0 and s == "WA":
        wa[int(p)-1] += 1
    elif ac[int(p)-1]==0 and s == "AC":
        ac[int(p)-1] = 1

acc = 0
waa = 0
for i in range(n):
    if ac[i] == 1:
        waa += wa[i]
        acc += 1

print(acc, waa)
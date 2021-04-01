# A問題

n, r = map(int, input().split())

if n >= 10:
    print(r)
else:
    print(100*(10-n)+r)

# B問題

n, k = map(int, input().split())

ans = 1
while n >= k:
    n = n // k
    ans += 1

print(ans)

#--------------------------------
# C問題

n = int(input())
x = list(map(int, input().split()))

a, b = min(x), max(x)
ans = 10**20

for i in range(a, b+1):
    count = 0
    for s in x:
        count += abs((s-i)**2)
    ans = min(ans, count)

print(ans)


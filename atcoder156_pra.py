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

# D問題
n, a, b = map(int, input().split())

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result

ans = 1
if (n-1)/2 == (n-1)//2:
    for i in range(1, ((n-1)/2)+1):
        ans += (cmb(n, i) * 2)
else:
    for s in range(1, ((n-1)//2)+1):
        ans += (cmb(n, s) * 2)
    ans += cmb(n, n//2)

print(ans)

ans -= (cmb(n,a) + cmb(n,b))

print(ans % ((10**9)+7))


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


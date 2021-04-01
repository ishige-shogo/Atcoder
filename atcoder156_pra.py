# A問題

n, r = map(int, input().split())

if n >= 10:
    print(r)
else:
    print(100*(10-n)+r)

# B問題

# 誤解答
n, k = map(int, input().split())

ans = 0
while True:
    n = n // k
    ans += 1
    if n < k:
        ans += 1
        print(ans)
        exit()

#--------------------------------
# C問題


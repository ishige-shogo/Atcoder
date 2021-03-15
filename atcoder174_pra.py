# A問題
x = int(input())

if x >= 30:
    print("Yes")
else:
    print("No")

#-------------------------------------------------------
# B問題

n, d = map(int, input().split())

count = 0
for _ in range(n):
    x, y = map(int, input().split())
    m = (x**2) + (y**2)
    if m**(1/2) <= d:
        count += 1

print(count)

#--------------------------------------------------------
# C問題

k = int(input())

if k % 2 == 0:
    print(-1)
    exit()

n = 1
m = 7
ans = 1

while True:
    if m % k == 0 and m >= k:
        print(ans)
        exit()
    m += (10**n)*7
    n += 1
    ans += 1

#---



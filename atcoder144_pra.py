# A問題

a, b = map(int, input().split())
if a <= 9 and b <= 9:
    print(a * b)
else:
    print(-1)

# B問題

n = int(input())
for i in range(1,10):
    for s in range(1,10):
        if n == i*s:
            print("Yes")
            exit()
print("No")

# C問題

n = int(input())

h = int(n**(0.5))

ans = 10**13

for i in range(1, h+1):
    if n % i == 0:
        m = n // i
        s = (m + i) - 2
        ans = min(s, ans)

print(ans)


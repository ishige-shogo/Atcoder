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

# D問題
import math

a, b, x = map(int, input().split())

if (a**2) * b == x:
    print(0)
    exit()

h = x / (a**2)

if h >= (b * 0.5):
    ans = math.degrees(math.atan(a / (2 * b - 2 * h)))
    print(90 - ans)
else:
    n = (2 * a * h) / b
    ans = math.degrees(math.atan(n / b))
    print(90 - ans)




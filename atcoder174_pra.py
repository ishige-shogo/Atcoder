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
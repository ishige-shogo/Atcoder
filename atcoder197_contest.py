s = input()

print(s[1]+s[2]+s[0])
#-----------------------------------------
h, w, x, y = map(int, input().split())

s = []
for _ in range(h):
    u = input()
    s.append(u)

count = 0

a, b = x-1, y-1

while a >= 0:
    if s[a][b] == "#":
        break
    else:
        count += 1
        a -= 1

a, b = x-1, y-1

while a <= h-1:
    if s[a][b] == "#":
        break
    else:
        count += 1
        a += 1

a, b = x-1, y-1

while b >= 0:
    if s[a][b] == "#":
        break
    else:
        count += 1
        b -= 1

a, b = x-1, y-1

while b <= w-1:
    if s[a][b] == "#":
        break
    else:
        count += 1
        b += 1

print(count-3)

#------------------------------------

n = int(input())
a = list(map(int, input().split()))

print(int(bin(1 | 5| 7), 2))

for i in range(2, n-1):
    x = a[:i]
    y = a[i:]
    for s in range(len(x)):


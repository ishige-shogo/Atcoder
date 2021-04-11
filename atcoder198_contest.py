
x, y = map(int, input().split())


n = int(input())

print(n-1)


# ---------

n = str(input())

u = n[::-1]

if u == n:
    print("Yes")
    exit()

cnt = 0
while cnt < 9:
    u += "0"
    m = u[::-1]
    if m == u:
        print("Yes")
        exit()
    cnt += 1

print("No")

#--------------------------------------

import math
r, x, y = map(int, input().split())

if x == 0 and y == 0:
    print(0)
    exit()

dist = ((x**2) + (y**2))**(1/2)

if dist < r:
    print(2)
    exit()

print(math.ceil(dist / r))

#----------------------------------------

n = int(input())
c = list(map(int, input().split()))

node = [[None, None, None]] * n

for _ in range(n-1):
    a, b = map(int, input().split())
    
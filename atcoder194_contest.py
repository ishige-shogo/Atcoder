
a, b = map(int, input().split())

if a+b >= 15 and b >= 8:
    print(1)
elif a+b >= 10 and b >= 3:
    print(2)
elif a+b >= 3:
    print(3)
else:
    print(4)

#-----------------------------------------------------

n = int(input())

v = [list(map(int,input().split())) for i in range(n)]

ary = []
for i in range(n):
    x = v[i][0]
    y = v[i][1]
    ary.append((x+y))

for s in range(n):
    for t in range(n):
        if s != t:
            ary.append(max(v[s][0],v[t][1]))

print(min(ary))

#---------------------------------------------------

n = int(input())
a = list(map(int, input().split()))

v = sum(a)
ans = 0
for i in range(n):
    ans += (a[i]**2)*(n-1)
    v -= a[i]
    ans -= (a[i] * v)*2

print(ans)

#----------------------------------------------------
import math

import sys
n = int(input())
t = n
ans = 1
while t > 0:
    ans *= t / n
    t -= 1
print(ans)


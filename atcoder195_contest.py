m, h = map(int, input().split())

if h % m == 0:
    print("Yes")
else:
    print("No")

#---------------------------------------------

import math
a, b, w = map(int, input().split())

n = math.ceil(w*1000/b)
x = math.floor(w*1000/a)

c = w*1000//b
d = w*1000//a

if (c == d) and (c*b != w*1000) and (d*a != w*1000):
    print("UNSATISFIABLE")
else:
    print(n, x)

#----------------------------------------------

n = int(input())

if n <= 999:
    ans = 0
elif n <= 999999:
    ans = n - 999
elif n <= 999999999:
    ans = (n - 999) + (n - 999999)
elif n <= 999999999999:
    ans = (n - 999) + (n - 999999) + (n - 999999999)
elif n <= 999999999999999:
    ans = (n - 999) + (n - 999999) + (n - 999999999) + (n - 999999999999)
else:
    ans = (n - 999) + (n - 999999) + (n - 999999999) + (n - 999999999999) + (n - 999999999999999)
print(ans)
#-----------------------------------------------

n, m, q = map(int, input().split())
ary = []
for i in range(n):
    w, v = map(int, input().split())
    ary.append((v, w))

x = list(map(int, input().split()))





for s in range(q):
    w, v = map(int, input().split())
    ary.append((v, w))

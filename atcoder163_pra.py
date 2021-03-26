# A問題

r = int(input())

print(2*3.1415*r)

#--------------------------------------------
# B問題

n, m = map(int, input().split())

a = list(map(int, input().split()))

s = sum(a)

if n >= s:
    print(n-s)
else:
    print(-1)

#----------------------------------------------
# C問題
# エラー
n = int(input())
a = list(map(int, input().split()))
a_p = a + [0]

p_a = [0] + a

p = []
h = a[0]
c = 0
for i in a_p:
    if h == i:
        c += 1
    else:
        p.append(c)
        h = i
        c = 1

p += [0]

f = -1
v = 0
for s in p_a:
    if s != f:
        print(p[v])
        v += 1
    else:
        print(0)
    f = s
#-------

import collections
n = int(input())
a = list(map(int, input().split()))

ca = collections.Counter(a)

for i in range(1, n+1):
    print(ca[i])
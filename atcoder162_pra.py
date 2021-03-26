# A問題

n = [int(s) for s in list(str(int(input())))]

if 7 in n:
    print("Yes")
else:
    print("No")

#---------------------------------------------
# B問題

n = int(input())

ans = 0
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        ans += i
print(ans)

#-----------------------------------------------
# C問題
import itertools
import math

k = range(1, 4)

m = itertools.product(k, repeat=3)

ans = 0
for i in m:
    ans += math.gcd(i[0], i[1], i[2])
print(ans)

#------
import math
k = int(input())

ans = 0
for s in range(1, k+1):
    for t in range(1, k+1):
        st = math.gcd(s, t)
        for u in range(1, k+1):
            stu = math.gcd(st, u)
            ans += stu
print(ans)

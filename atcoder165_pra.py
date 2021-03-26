# A問題

k = int(input())
a, b = map(int, input().split())

for i in range(a,b+1):
    if i % k == 0:
        print("OK")
        exit()
print("NG")

#----------------------------------------------------
# B問題

from decimal import Decimal
x = int(input())

money = 100
ans = 0
while money < x:
    ans += 1
    # money = int(Decimal(money*1.01))だと失敗する
    money = money * 101 //100

print(ans)

from decimal import Decimal
i = "245673867548237383733920.9303725374845243748"

print(int(Decimal(i)))

p = 234156738956839.9
print(int(p))

i = 5.90
print(int(i))

i = 3141592653589793238462643383279
print(int(i))

import math
i = 314159265358979323.8462643383279
print(math.floor(i))

from decimal import Decimal
x = 314159265358979323.8462643383279
print(str(x))
print(int(Decimal(x)))

from decimal import Decimal
x = "314159265358979323.8462643383279"
print(int(Decimal(x)))

#---------------------------------------
# C問題

import itertools

n, m, q = map(int, input().split())

ary = []
for _ in range(q):
    a, b, c, d = map(int, input().split())
    ary.append((a-1,b-1,c,d))

A = list(itertools.combinations_with_replacement(range(1,m+1), n))


ans = 0

for i in A:
    count = 0
    for s in ary:
        if i[s[1]] - i[s[0]] == s[2]:
            count += s[3]
    ans = max(ans, count)

print(ans)



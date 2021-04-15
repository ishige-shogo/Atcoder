# A問題
r = int(input())
print(r**2)

# B問題

n = int(input())
s = input()

if n % 2 != 0:
    print("No")
    exit()

m = n//2

if s[:m] == s[m:]:
    print("Yes")
else:
    print("No")

# C問題

import itertools
n = int(input())
p = itertools.permutations(range(0,n), r=None)
ary = []
for _ in range(n):
    x, y = map(int, input().split())
    ary.append([x, y])

dist = 0
count = 0
for i in p:
    for s in range(n-2):
        a = i[s]
        b = i[s+1]
        dist += ((ary[a][0] - ary[b][0])**2 + (ary[a][1] - ary[b][1])**2)**(1/2)
    count += 1
print(dist / count)



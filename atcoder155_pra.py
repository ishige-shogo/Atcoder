# A問題

a, b, c = map(int, input().split())

if a == b and a == c:
    print("No")
elif a == b:
    print("Yes")
elif b == c:
    print("Yes")
elif a == c:
    print("Yes")
else:
    print("No")

# B問題

n = int(input())
a = list(map(int, input().split()))


for i in a:
    if i % 2 == 0:
        if (i % 3 != 0) and (i % 5 != 0):
            print("DENIED")
            exit()

print("APPROVED")

# C問題
n = int(input())
ary = {}
ma = 1
for _ in range(n):
    k = input()
    if k in ary:
        ary[k] += 1
        ma = max(ma, ary[k])
    else:
        ary[k] = 1
l = []

for i in ary:
    if ary[i] == ma:
        l.append(i)
l.sort()
for i in l:
    print(i)

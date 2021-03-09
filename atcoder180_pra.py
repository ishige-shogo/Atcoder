# A問題

n, a, b = map(int, input().split())

print(n - a + b)

#----------------------------------------------
# B問題

n = int(input())

x = list(map(int, input().split()))

man = 0
yuk = 0
tyb = 0

for i in x:
    man += abs(i)

for s in x:
    yuk += s**2
yuk = yuk ** (1/2)

for v in x:
    tyb = max(tyb, abs(v))

print(man)
print(yuk)
print(tyb)


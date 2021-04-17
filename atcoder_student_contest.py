x, y, z = map(int, input().split())

if z*y/x == z*y//x:
    print(int(z*y/x-1))
else:
    print(z*y//x)

#-----------------------

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = list(set(a) ^ set(b))

L=[str(a) for a in c]
L=" ".join(L)
print(L)

#--------------------------------------

a, b = map(int, input().split())

ans = 1
for i in range(1, b+1):
    if (b//i-1)*i >= a:
        ans = i

print(ans)

#-------------

n, p = map(int, input().split())


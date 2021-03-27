# A問題

x, y, z = map(int, input().split())

x, y, z = z, x, y

print(x, y, z)

#---------------------------------------------
# B問題

n, m = map(int, input().split())

a = sorted(list(map(int, input().split())), reverse=True)

if a[m-1] < sum(a)*(1/(4*m)):
    print("No")
else:
    print("Yes")

#-------------------------------------------------
# C問題

n, k = map(int, input().split())

s = (n // k) + 1

if n % k == 0:
    print(0)
    exit()

ans = min((n%k),abs(n-(s*k)))

print(ans)
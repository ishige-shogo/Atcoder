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
    
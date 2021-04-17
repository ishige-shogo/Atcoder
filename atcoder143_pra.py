# A問題

a, b = map(int, input().split())

l = a - (2*b)

if l <= 0:
    print(0)
else:
    print(l)

# B問題

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans += (sum(a) - i) * i
print(ans//2)

#別解
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    for s in range(i+1, n):
        ans += a[i]*a[s]
print(ans)


# C問題

n = int(input())
s = input()

color = ""
ans = 0
for i in range(n):
    if color != s[i]:
        ans += 1
    color = s[i]
print(ans)
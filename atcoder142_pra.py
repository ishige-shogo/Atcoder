# A問題

n = int(input())
if n % 2 == 0:
    print(1/2)
else:
    print((n//2+1)/n)


# B問題

n, k = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
for i in range(n):
    if h[i] >= k:
        ans += 1

print(ans)


# C問題

n = int(input())
a = list(map(int, input().split()))

ans = [0] * n
for i in range(n):
    ans[a[i]-1] = i+1

L=[str(a) for a in ans]
L=" ".join(L)
print(L)





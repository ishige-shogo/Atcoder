
# A問題

n = int(input())

print(n**3)


# B問題

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = sum(b)
pre = -1
for i in a:
    if pre + 1 == i:
        ans += c[pre-1]
    pre = i

print(ans)


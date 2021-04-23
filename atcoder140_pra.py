
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

# C問題

n = int(input())
b = list(map(int, input().split()))

225

ans = [b[0]]

for i in range(1, n):
    if b[i] >= b[i-1]:
        ans.append(b[i-1])
    else:


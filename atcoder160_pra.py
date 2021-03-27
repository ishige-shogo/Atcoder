# A問題

s = input()

if s[2]==s[3] and s[4]==s[5]:
    print("Yes")
else:
    print("No")

# B問題

x = int(input())

a = x // 500
y = x % 500

b = y // 5

print((a*1000) + (b*5))

# C問題

k, n = map(int, input().split())

a = list(map(int, input().split()))

a += [k]

dis = [a[0]]

for i in range(n):
    dis.append(a[i+1] - a[i])


print(min(a[n-1] - a[0], sum(dis) - max(dis)))
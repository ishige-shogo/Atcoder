# A問題

s = input()
week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
print(7 - week.index(s))

# B問題

n = int(input())
s = input()

ans = ""
for i in s:
    m = ord(i) + n
    if m > 90:
        ans += chr(64 + (m - 90))
    else:
        ans += chr(ord(i) + n)

print(ans)

# C問題

a, b, x = map(int, input().split())

left, right = 0, 10**9+1

while left+1 < right:
    middle = (left + right) // 2
    if x >= (a * middle) + (b * len(str(middle))):
        left = middle
    else:
        right = middle
print(left)

# D問題

n = int(input())
point = []
for i in range(n):
    point.append([0])
ans = []
for _ in range(n-1):
    a, b = map(int, input().split())
    num = 1
    while True:
        if (num not in point[a-1]) and (num not in point[b-1]):
            point[a-1].append(num)
            point[b-1].append(num)
            break
        else:
            num += 1
    ans.append(num)

print(max(ans))
for i in ans:
    print(i)

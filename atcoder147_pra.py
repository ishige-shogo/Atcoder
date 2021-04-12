# A問題

a, b, c = map(int, input().split())

if a+b+c >= 22:
    print("bust")
else:
    print("win")

# B問題

s = input()

rs = s[::-1]

ans = 0
for i in range(len(s)):
    if s[i] != rs[i]:
        ans += 1

print(ans/2)
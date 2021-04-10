# A問題

k, x = map(int, input().split())

if x <= k*500:
    print("Yes")
else:
    print("No")

# B問題

n = int(input())
s = input()

ans = 0
for i in range(n-3):
    v = s[i] + s[i+1] + s[i+2]
    if v == "ABC":
        ans += 1

print(ans)
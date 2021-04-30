# A問題

a = int(input())
s = input()
if a >= 3200:
    print(s)
else:
    print("red")

# B問題

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans += i ** -1
print(ans ** -1)


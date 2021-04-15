# A問題
r = int(input())
print(r**2)

# B問題

n = int(input())
s = input()

if n % 2 != 0:
    print("No")
    exit()

m = n//2

if s[:m] == s[m:]:
    print("Yes")
else:
    print("No")


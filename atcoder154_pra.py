# A問題

s, t = map(str, input().split())
a, b = map(int, input().split())
u = input()

if s == u:
    a -= 1
else:
    b -= 1

print(a, b)

# B問題

s = input()
print("x" * len(s))

# C問題

n = int(input())
a = list(map(int, input().split()))

b = set(a)

if len(a) == len(b):
    print("YES")
else:
    print("NO")

# A問題
a = input()
if a.islower():
    print("a")
else:
    print("A")

# B問題

n, k = map(int, input().split())

p = sorted(list(map(int, input().split())))

print(sum(p[0:k]))


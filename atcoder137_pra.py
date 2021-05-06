#A問題

a, b = map(int, input().split())
x = a + b
y = a - b
z = a * b
print(max(x, y, z))

# B問題

k, x = map(int, input().split())
a = list(range(x-k+1, k+x))
print(*a)


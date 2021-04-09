# A問題

n, m = map(int, input().split())
if n == m:
    print("Yes")
else:
    print("No")

# B問題

n, m = map(int, input().split())
if n >= m:
    print(str(m)*n)
else:
    print(str(n)*m)
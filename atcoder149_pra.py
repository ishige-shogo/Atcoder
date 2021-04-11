
# A問題

s, t = map(str, input().split())
print(t+s)

# B問題

a, b, k = map(int, input().split())

if a >= k:
    print(a-k, b)
elif (a+b) >= k:
    print(0, b-(k-a))
else:
    print(0, 0)

# C問題

x = int(input())

def is_prime(n):
    if n == 2:
        return True
    h = n//2
    for i in range(2, h+1):
        if n % i == 0:
            return False
    return True

for s in range(x, 100004):
    if is_prime(s):
        print(s)
        exit()

# D問題

n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

j = ""
point = 0

for i in range(n):
    if t[i] == "r":
        j += "p"
    elif t[i] == "p":
        j += "s"
    else:
        j += "r"

print(j)
print(point)

for s in range(k, n):
    if j[s] == j[s-k]:
        j[s] == "o"
        
s = input()

print(s[1]+s[2]+s[0])
#-----------------------------------------
h, w, x, y = map(int, input().split())

s = []
for _ in range(h):
    u = input()
    s.append(u)

count = 0

a, b = x-1, y-1

while a >= 0:
    if s[a][b] == "#":
        break
    else:
        count += 1
        a -= 1

a, b = x-1, y-1

while a <= h-1:
    if s[a][b] == "#":
        break
    else:
        count += 1
        a += 1

a, b = x-1, y-1

while b >= 0:
    if s[a][b] == "#":
        break
    else:
        count += 1
        b -= 1

a, b = x-1, y-1

while b <= w-1:
    if s[a][b] == "#":
        break
    else:
        count += 1
        b += 1

print(count-3)

#------------------------------------

n = int(input())
a = list(map(int, input().split()))

print(int(bin(1 | 5| 7), 2))

for i in range(2, n-1):
    x = a[:i]
    y = a[i:]
    for s in range(len(x)):
        exit
#---------------------

N = int(input())
A = list(map(int, input().split()))

ans = 1 << 30
for bit in range(1 << N-1):
    memo_xor = 0
    memo_or = A[0]
    for i in range(N):
        if (bit >> (N-1)-i) & 1:
            memo_xor ^= memo_or
            memo_or = A[i]
        else:
            memo_or |= A[i]
    memo_xor ^= memo_or
    ans = min(ans, memo_xor)
print(ans)
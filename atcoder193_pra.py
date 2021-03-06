# A問題

a, b = map(int, input().split())

print(((a - b)/a)*100)

#----------------------------------------------------------
# B問題

n = int(input())

game = []
v = 10**9+1
for _ in range(n):
    a, p, x = map(int, input().split())
    if a < x:
        v = min(v, p)

if v == 10**9+1:
    print(-1)
else:
    print(v)
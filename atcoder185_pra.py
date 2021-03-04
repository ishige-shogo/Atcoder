# A問題

a, b, c, d = map(int, input().split())

print(min(a,b,c,d))

#---------------------------------------------------------------
# B問題

n, m, t = map(int, input().split())

ary = []
for i in range(m):
    a, b = map(int, input().split())
    ary.append((a, b))

battery = n
battery -= ary[0][0]
if battery <= 0:
    print("No")
    exit()

for u in range(m-1):
    battery += (ary[u][1] - ary[u][0])
    if battery > n:
        battery = n
    battery -= (ary[u+1][0] - ary[u][1])
    if battery <= 0:
        print("No")
        exit()

battery += (ary[m-1][1] - ary[m-1][0])
if battery > n:
    battery = n
battery -= (t - ary[m-1][1])
if battery <= 0:
    print("No")
    exit()

print("Yes")



# A問題
a, b, c, d, e = map(int, input().split())

x = [a, b, c, d, e]

for i in range(x):
    if x[i] == 0:
        print(i+1)

#-----------------------------------------------------
# B問題

x, y = map(int, input().split())

for i in range(x+1):
    s = x - i
    if y == (i*2) + (s*4):
        print("Yes")
        exit()

print("No")


#----------------------------------------------------
# C問題

x, n = map(int, input().split())

if n == 0:
    print(x)
    exit()

p = list(map(int, input().split()))

if x not in p:
    print(x)
    exit()

con = 1
while True:
    ans = x - con
    if ans not in p:
        print(ans)
        exit()
    ans = x + con
    if ans not in p:
        print(ans)
        exit()
    con += 1

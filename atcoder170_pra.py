
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


for i in range(101):
    if i not in p:
        



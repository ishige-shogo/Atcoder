# A問題

s, w = map(int, input().split())

if s <= w:
    print("unsafe")
else:
    print("safe")

#---------------------------------------------------
# B問題

a, b, c, d = map(int, input().split())

while ((a > 0) and (c > 0)):
    c -= b
    if c <= 0:
        print("Yes")
        exit()
    a -= d
    if a <= 0:
        print("No")
        exit()

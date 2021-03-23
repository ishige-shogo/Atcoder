# A問題

n = int(input())

num_a = str(n)
list_num_a = list(num_a)
a_list = [int(s) for s in list_num_a]

if a_list[-1] == 3:
    print("bon")
elif (a_list[-1] == 0) or(a_list[-1] == 1) or(a_list[-1] == 6) or(a_list[-1] == 8):
    print("pon")
else:
    print("hon")

#-----------------------------------------------------
# B問題

k = int(input())
s = input()

if len(s) <= k:
    print(s)
else:
    print(s[:k] + "...")

#-----------------------------------------------------
# C問題
import math
a, b, h, m = map(int, input().split())

h = (h * 30) + (m * 0.5)
m *= 6

if abs(m - h) > 180:
    r = 360 - abs(m - h)
else:
    r = abs(m - h)

# 余弦定理
# a**2 + b**2 - 2ab * cos c = c**2
ans = ((a**2) + (b**2) - ((2*a*b)*(math.cos(math.radians(r)))))**(0.5)

print(ans)
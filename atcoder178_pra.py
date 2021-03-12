# A問題

x = int(input())

if x == 1:
    print(0)
else:
    print(1)

#----------------------------------------------------
# B問題
a, b, c, d = map(int, input().split())

# 正ｘ正、負ｘ負の大きい方
if (b >= 0 and d >= 0) or (a < 0 and c < 0):
    print(max(b * d, a * c))
# 正ｘ負、正ｘ負の大きい方
else:
    print(max(a * d, b * c))


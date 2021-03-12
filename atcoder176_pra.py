# A問題
import math

n, x, t = map(int, input().split())

print(math.ceil(n/x) * t)

#-------------------------------------------------------
# B問題

n = int(input())

if n % 9 == 0:
    print("Yes")
else:
    print("No")

#----------------------------------------------------------
# C問題

n = int(input())
a = list(map(int, input().split()))

step = 0
# 配列の連続した２つの要素を比べる
# 前の要素の数値が高い場合、stepをカウントし、要素を書き換える
for i in range(n-1):
    if a[i] > a[i+1]:
        step += a[i] - a[i+1]
        a[i+1] = a[i]

print(step)
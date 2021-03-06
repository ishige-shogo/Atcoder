# A問題

a, b = map(int, input().split())

print(((a - b)/a)*100)

#----------------------------------------------------------
# B問題

# ゲームショップの件数
n = int(input())

# vの初期値はpの範囲外
v = 10**9+1

for _ in range(n):
    a, p, x = map(int, input().split())
    if a < x:
        # 価格が小さいものに更新される
        v = min(v, p)

# 初期値から変化しなければ、ゲームを買えないことになる
if v == 10**9+1:
    print(-1)
else:
    print(v)


#--------------------------------------------------------------
# C問題
import math
# 整数ｎ
n = int(input())
# ２乗した時にn以上となる最小値m
m = math.floor(n**(1/2))

# iのs乗がn以下であるものをリスト化
number = []
for i in range(2, m+1):
    s = 2
    while True:
        if i ** s > n:
            break
        number.append(i**s)
        s += 1
# 重複した数値を除いたnumber配列の要素数を、全体から引いたものを出力
print(n-len(set(number)))


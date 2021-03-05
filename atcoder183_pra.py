# A問題

x = int(input())

if x >= 0:
    print(x)
else:
    print(0)

#-----------------------------------------------------------
# B問題

# 座標(a, b)から座標(c, d)に向けてビリヤードの球を打つ
a, b, c, d = map(int, input().split())

# 相似な三角形の性質を利用。三角形のx軸上の部分に当たる辺の長さを計算
x = (b / (b + d)) * abs(c - a)

# a, cの大小によって射出する方向が異なるので条件分岐
if a < c:
    print(a + x)
else:
    print(a - x)

#-------------------------------------------------------------
# C問題

# 全ての順序パターンを組み合わせで使用
import itertools

# n, k = 都市数, 想定移動時間
n, k = map(int, input().split())
# 各都市間の移動時間
t = [list(map(int,input().split())) for i in range(n)]
# 1から(n-1)までの連番を配列化
city_number = list(range(1, n))
# 全ての順序パターンをイテレート
city = list(itertools.permutations(city_number))

count = 0

# tをもとに、各順列パターンでの移動時間を計算
for i in city:
    sum = 0
    # 都市１から最初の都市jにかかる移動時間
    sum += t[0][i[0]]
    # 都市iから都市jにかかる移動時間
    for s in range(n-2):
        sum += t[i[s]][i[s+1]]
    # 都市iから都市１にかかる移動時間
    sum += t[i[n-2]][0]
    # 移動時間の合計がkとなればカウントする
    if sum == k:
        count += 1
print(count)

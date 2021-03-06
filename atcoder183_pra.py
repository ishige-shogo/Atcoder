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

#---------------------------------------------------------
# D問題

# 解法１(実行時間エラー)
n, w = map(int, input().split())

s = [list(map(int,input().split())) for i in range(n)]

water = [0]*(2*(10**5)+1)

for i in range(n):
    for c in range(s[i][0], s[i][1]):
        water[c] += s[i][2]
        if water[c] > w:
            print("No")
            exit()
print("Yes")


# 解法２：上記の改良バージョン(実行時間エラー)
n, w = map(int, input().split())

water = [0]*(2*(10**5)+1)

for i in range(n):
    s, t, p = map(int, input().split())
    for c in range(s, t):
        water[c] += p

for z in water:
    if z > w:
        print("No")
        exit()
print("Yes")

# 解法３

# N, W = 人数, 毎分の供給量
N, W = map(int, input().split())
# 時刻sにpのお湯が必要になり、時刻tにpのお湯が不要になる
event = []
for i in range(N):
    s, t, p = map(int, input().split())
    event.append((s, p))
    event.append((t, -p))
# 時刻順に並び替える
event.sort()

# event配列をもとに、カウントを増減していく。途中でWを超えたら終了。
val = 0
for t, v in event:
    val += v
    if val > W:
        print("No")
        exit()
print("Yes")


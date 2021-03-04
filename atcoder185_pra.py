# A問題

a, b, c, d = map(int, input().split())

print(min(a,b,c,d))

#---------------------------------------------------------------
# B問題

#n, m, t = バッテリー残量, 充電スポット数, 帰宅時間
n, m, t = map(int, input().split())

#a, b = 充電開始時刻, 充電終了時刻
ary = []
for i in range(m):
    a, b = map(int, input().split())
    ary.append((a, b))

#最初の充電スポットまでのバッテリー残量(0以下になったら終了)
battery = n
battery -= ary[0][0]
if battery <= 0:
    print("No")
    exit()

#最初の充電スポットから最後の充電スポットに入るまでのバッテリー残量(0以下になったら終了)
for u in range(m-1):
    battery += (ary[u][1] - ary[u][0])
    #バッテリー残量が容量を上回ったら、容量を上限とする
    if battery > n:
        battery = n
    battery -= (ary[u+1][0] - ary[u][1])
    if battery <= 0:
        print("No")
        exit()

#最後の充電スポットから帰宅までのバッテリー残量(0以下になったら終了)
battery += (ary[m-1][1] - ary[m-1][0])
if battery > n:
    battery = n
battery -= (t - ary[m-1][1])
if battery <= 0:
    print("No")
    exit()

#バッテリー残量が0以下にならなかった場合(プログラムが終了しなかった)
print("Yes")

#--------------------------------------------------------
# C問題

L = int(input())
#組み合わせの数：nCr コンビネーションのメソッド
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result

#植木算(仕切りを入れるパターン数を計算)
print(cmb(L-1,11))

#------------------------------------------------------------
# D問題

#切り上げメソッド用
import math

# n, m = 全体のマス数, 青色のマス数
n, m = map(int, input().split())

# 青マスが0のとき、1回の押印で終了
if m == 0:
    print(1)
    exit()
# 全てが青マスのとき、1回も押印せずに終了
elif m == n:
    print(0)
    exit()

# 小さい数値順に配列
a = sorted(list(map(int, input().split())))

# 青マス間の白マス数を記録(ただし0は除く)
bet = []

if (a[0] - 1) != 0:
    bet.append(a[0] - 1)

if m >= 2:
    for i in range(m - 1):
        if (a[i+1] - a[i] - 1) != 0:
            bet.append(a[i+1] - a[i] - 1)
    if (n - a[m-1]) != 0:
        bet.append(n - a[m-1])

# bet配列の最小値がスタンプの大きさになる
stamp = min(bet)

# 白マスにスタンプを押していく最小の回数を計算
ans = 0
for s in bet:
    ans += math.ceil(s / stamp)

print(ans)


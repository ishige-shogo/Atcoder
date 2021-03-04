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


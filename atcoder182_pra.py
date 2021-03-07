# A問題
A, B = map(int, input().split())
print(((2*A)+100)-B)

#--------------------------------------------------------
# B問題

# 数列の要素数
n = int(input())
# 数列
a = list(map(int, input().split()))

# 最大のgcd度を記録
gcd = 0
for i in range(2, (max(a)+1)):
    count = 0
    # 割り切れたらカウントしていく
    for s in a:
        if s % i == 0:
            count += 1
    # 記録されているgcd度より大きい場合、ansとgcdを更新
    if max(count, gcd) == count:
        ans = i
    gcd = max(count, gcd)

print(ans)

#----------------------------------------------------------
# C問題

# 任意の整数N
n = int(input())

# 1桁ずつ数字を分割してリスト化
num_a = str(n)
list_num_a = list(num_a)
a_list = [int(s) for s in list_num_a]

# Nが1桁で、3で割り切れない場合は不可能
if len(a_list) == 1 and n % 3 != 0:
    print(-1)
    exit()

# Nが2桁で、各桁の数字を3で割ったときの余りが2つとも同じ場合は不可能(余り0を除く)
if len(a_list) == 2:
    w = a_list[0] % 3
    y = a_list[1] % 3
    if (w == 1 and y == 1) or (w == 2 and y == 2):
        print(-1)
        exit()

# 各桁の合計値が3で割り切れる場合、消去する桁は0
if sum(a_list) % 3 == 0:
    print(0)
    exit()
# 各桁の合計値を3で割ったときの余りが1のとき、各桁の数字を3で割ったときの余りが1のものが存在する場合に、その数字1つを消去することで可能
elif sum(a_list) % 3 == 1:
    for i in a_list:
        if i % 3 == 1:
            print(1)
            exit()
# 各桁の合計値を3で割ったときの余りが2のとき、各桁の数字を3で割ったときの余りが2のものが存在する場合に、その数字1つを消去することで可能
elif sum(a_list) % 3 == 2:
    for s in a_list:
        if s % 3 == 2:
            print(1)
            exit()
# 上記のいずれにも合致しない場合、2つの数字を消去することで可能
print(2)

#-----------------------------------------------------------
# D問題

# 解法１：単純バージョン(実行時間エラー)
n = int(input())
a = list(map(int, input().split()))

robot = 0
ans = 0
for i in range(n):
    for s in range(0,(i+1)):
        robot += a[s]
        ans = max(ans, robot)
print(ans)

# 解法２
# 数列の要素数
n = int(input())
# 数列
a = list(map(int, input().split()))

# point, robot, ans, v = 1行動の最大値, 1行動終了時のロボットの座標, 座標の最大値, 1行動を全て終えたときの移動値
point = 0
robot = 0
ans = 0
v = 0
for s in range(n):
    v += a[s]
    point = max(point, v)
    robot_max = robot + point
    ans = max(ans, robot_max)
    robot += v
print(ans)

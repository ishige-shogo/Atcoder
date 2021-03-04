# A問題

a, b = map(int, input().split())
c, d = map(int, input().split())
print((a*d)-(b*c))

#-------------------------------------------------------
# B問題

# n, x = 問題数, 最初の持ち点
n, x = map(int, input().split())
s = str(input())

for i in range(n):
    # oの場合１点プラス
    if s[i] == "o":
        x += 1
    # xの場合、現在の点数が0点でない場合にのみマイナス１点
    elif s[i] == "x" and x != 0:
        x -= 1
print(x)

#---------------------------------------------------------
# C問題

# a, b, c, d = 座標(a, b)から座標(c, d)に駒を移動する
a, b = map(int, input().split())
c, d = map(int, input().split())

# どの場合でも3手以内に移動が可能
# 移動前後の座標が同じの場合、駒を動かさずに終了(0手)
if (a==c)and(b==d):
    print(0)
# 「斜線上」または「周囲３マス」の場合、1手で終了
elif (a+b==c+d)or(a-b==c-d)or(abs(a-c)+abs(b-d)<=3):
    print(1)
# 「3マス移動後の3マス移動」または「3マス移動後の斜線上(斜線移動後の周囲3マス)」または「斜線移動後の斜線上」の場合、2手で終了
elif (abs(a-c)+abs(b-d)<=6)or(abs(abs(a-c)-abs(b-d))<=3)or((abs(abs(a-c)-abs(b-d)))%2==0):
    print(2)
# 上記に合致しない場合は、必ず3手で終了する
else:
    print(3)


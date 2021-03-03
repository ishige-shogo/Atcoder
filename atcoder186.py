#---------------------------------------------------------
# A問題

N, W = map(int, input().split())
print(N//W)

#----------------------------------------------------------
# B問題

H, W = map(int, input().split())
A = [list(map(int,input().split())) for i in range(H)]
# 作成したA配列の集合体を全て展開して１つの配列Bにする
B = []
for h in range(H):
    for w in range(W):
        num = A[h][w]
        B.append(num)
# 配列Bの数値の合計値から、Bの最小数値とBの要素数を掛けたものを引く
print(sum(B) - (min(B) * len(B)))

#-----------------------------------------------------------
# C問題
N = int(input())

# 1から検索する方法(数値iを文字列と８進数表記にし、いずれかに７が含まれているものをリストアップする)
m = []
for i in range(N):
    oct_num = oct(i + 1)
    str_num = str(i + 1)
    if ("7" in str_num) or ("7" in oct_num):
        m.append(i + 1)
#全体からリストアップされた要素の個数を引く
print(N - len(m))

#------------------------------------------------------------
# D問題

#解法１：単純バージョン(実行時間エラー)
N = int(input())
A = list(map(int, input().split()))
# １つずつ計算し、合計していく
sum = 0
for s in range(N):
    for t in list(range(s+1,N)):
        sum += abs(A[s] - A[t])
print(sum)


#解法２：試行回数を減らす(計算をまとめる)バージョン
N = int(input())
A = list(map(int, input().split()))
#要素を小さい順に並べ替える
a = sorted(A)
# a = [D, C, B, A]のとき
#(3A-0A)+(2B-1B)+(1C-2C)+(0D-3D)が問題の合計値になる
sum = 0
for s in range(N):
    v = N - s - 1
    num = (s * a[s]) - (s * a[v])
    sum += num
print(sum)


#-----------------------------------------------------------
# E問題

#解法１：単純バージョン(実行時間エラー)
T = int(input())
V = [list(map(int,input().split())) for i in range(T)]

for i in range(T):
    m = 1
    while True:
        if (((V[i][2] * m) + V[i][1]) % V[i][0]) == 0:
            print(m)
            break
        m += 1

#------
#試行中
T = int(input())
V = [list(map(int,input().split())) for i in range(T)]

#一周で試行が終わる
(V[i][0] - V[i][1]) % V[2] == 0
#永遠にできない
V[i][0] % V[i][2] == 0


def circle(n, k):
    n = n
    x = n % k
    if x == 0:
        print(-1)
    elif x == 1:
        print("ok")
    else:
        circle(n, x)

print(circle(8,3))

print(8 %3)

#-------------

# N,S,K
#(Km + S) と N の最小公倍数

num1=684
num2=1134

#ユークリッドの互除法
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

#最小公倍数
def lcm(a,b):
    return int(a*b/gcd(a,b))

print(gcd(num2,num1))
print(lcm(num1,num2))
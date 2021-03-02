n = int(input())
x, y = map(int, input().split())
a = list(map(int, input().split()))

# 数値を一桁ずつ分割
num_a = str(n)
list_num_a = list(num_a)
a_list = [int(s) for s in list_num_a]

xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))

#-------------------------------------------------
# A問題

A, B = map(int, input().split())
num_a = str(A)
num_b = str(B)
list_num_a = list(num_a)
a_list = [int(s) for s in list_num_a]
list_num_b = list(num_b)
b_list = [int(s) for s in list_num_b]

if sum(a_list) > sum(b_list):
    print(sum(a_list))
else:
    print(sum(b_list))

#-------------------------------------------------
# B問題

n = int(input())
ary = []
for i in range(n):
    x, y = map(int, input().split())
    ary.append((x, y))

# 1つずつ検証する方法
count = 0
for s in range(n):
    for t in list(range(s+1,n)):
        # (y座標の差 / x座標の差) が直線の傾き
        c = ary[s][1] - ary[t][1]
        m = ary[s][0] - ary[t][0]
        ans = c / m
        # 条件に合っていたものを１つずつカウント
        if (-1 <= ans) and (ans <= 1):
            count += 1
print(count)

#-----------------------------------------------------
# C問題
#解法１：ごり押しパターン(処理時間エラー)
n = int(input())
ary = []
for i in range(n):
    s = str(input())
    ary.append(s)

a_line = []
b_line = []

for v in range(n):
    if ary[v][0] == "!":
        txt = ary[v][1:]
        a_line.append(txt)
    else:
        b_line.append(ary[v])

for u in a_line:
    if u in b_line:
        print(u)
        exit()

print("satisfiable")

#上記の少し改良パターン(処理時間エラー)
#処理時間を確認したら上記より長くなりました(改悪)

n = int(input())
ary = []
for i in range(n):
    s = str(input())
    ary.append(s)

a_line = []
b_line = []

for v in range(n):
    if ary[v][0] == "!":
        txt = ary[v][1:]
        if txt in b_line:
            print(txt)
            exit()
        a_line.append(txt)
    else:
        if ary[v] in a_line:
            print(ary[v])
            exit()
        b_line.append(ary[v])

print("satisfiable")

#解法２：重複の文字列を排除する(処理時間エラー)

n = int(input())
ary = []
for i in range(n):
    s = str(input())
    ary.append(s)

wop = list(set(ary))
m = len(wop)

for v in range(m):
    if wop[v][0] == "!":
        wop[v] = wop[v][1:]


for w in wop:
    if wop.count(w) == 2:
        print(w)
        exit()

print("satisfiable")


#解法３：解法１と２のミックス簡単バージョン

n = int(input())
# 重複した要素を除いたリストを作成
s = set(input() for i in range(n))
# 先頭に！がついていた場合、それを除いた文字列が配列に存在するときに、その文字を出力(+プログラムの終了)
for v in s:
    if v[0] == "!":
        if v[1:] in s:
            print(v[1:])
            exit()
# 該当しない場合はこれを出力
print("satisfiable")


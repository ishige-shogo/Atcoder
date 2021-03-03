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

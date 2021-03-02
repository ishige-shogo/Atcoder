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

# A問題

a, b = map(int, input().split())

print(((a - b)/a)*100)

#----------------------------------------------------------
# B問題

# ゲームショップの件数
n = int(input())

# vの初期値はpの範囲外
v = 10**9+1

for _ in range(n):
    a, p, x = map(int, input().split())
    if a < x:
        # 価格が小さいものに更新される
        v = min(v, p)

# 初期値から変化しなければ、ゲームを買えないことになる
if v == 10**9+1:
    print(-1)
else:
    print(v)

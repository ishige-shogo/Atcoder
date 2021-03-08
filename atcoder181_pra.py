# A問題
n = int(input())

if n % 2 == 0:
    print("White")
else:
    print("Black")
#-------------------------------------------------------------
# B問題

# 解法１：実行時間エラー
n = int(input())

ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += sum(range(a, b+1))

print(ans)

# 解法２
# 操作回数
n = int(input())
# 数列の要素をすべて足した時の計算
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += ((b+a)/2)*(b-a+1)
print(int(ans))

#--------------------------------------------------------------
# C問題

# 点の数
n = int(input())
# 各座標をリスト化
v = [list(map(int,input().split())) for i in range(n)]

# (a, b)(c, d)の傾きと(a, b)(e, f)の傾きが同じ場合、(a, b)(c, d)(e, f)の３点は同一直線上
for s in range(n):
    for t in range(s+1,n):
        for i in range(t+1,n):
            a = (v[t][1]-v[s][1])*(v[i][0]-v[s][0])
            b = (v[t][0]-v[s][0])*(v[i][1]-v[s][1])
            if a == b:
                print("Yes")
                exit()
print("No")
        
    

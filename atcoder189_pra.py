# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())
# スペース区切りの整数の入力
b, c = map(int, input().split())
# 文字列の入力
s = input()
# 出力
print("{} {}".format(a+b+c, s))

for i in range(n):
    a, b = map(int, input().split())

A = list(map(int, input().split()))

#------------------------------------------------------

num = input()

if num[0]==num[1] and num[1]==num[2]:
    print("Won")
else:
    print("Lost")

#-----------------------------------------------------

n, x = map(int, input().split())

amount = 0
for i in range(n):
    v, p = map(int, input().split())
    amount += v * p
    if amount > x*100:
        print(i+1)
        exit()
print(-1)

#--------------------------------------------------------
#実行時間超過エラー

n = int(input())
a = list(map(int, input().split()))

# (r-l+1)*x が最大になるとき
# x = min(a[(l-1):r])

r, orange = 1, 0

while r <= n:
    l = 1
    while l <= r:
        x = min(a[(l-1):r])
        if orange < (r-l+1)*x:
            orange = (r-l+1)*x
        l += 1
    r += 1

print(orange)

#pypyバージョン(こっちのほうが処理が速い)

N = int(input())
A = list(map(int,input().split()))

ans=0
# １つずつ確認していく方法
for i in range(0,N):
    x=A[i]
    for k in range(i,N):
        # xの値を記録しておく(２つを比べ、小さいほうをxとする)
        x=min(A[k],x)
        # 答えを更新していく
        ans = max(x*(k-i+1),ans)
print(ans)

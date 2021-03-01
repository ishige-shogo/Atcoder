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
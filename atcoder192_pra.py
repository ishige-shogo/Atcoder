# A問題
import math

x = int(input())

y = math.floor(x/100)

print((y+1)*100-x)

#------------------------------------------------------
# B問題
# 文字列ｓ
s = str(input())
# 文字列ｓを１文字ずつ検証。「奇数番目で大文字」か「偶数番目で小文字」の場合、判定はNoになる
for i in range(len(s)):
    if i % 2 == 0:
        if s[i].isupper():
            print("No")
            exit()
    else:
        if s[i].islower():
            print("No")
            exit()
print("Yes")

#-----------------------------------------------------
# C問題

n, k = map(int, input().split())

def kap(num):
    num_a = str(num)
    list_num_a = list(num_a)
    a_list = [int(s) for s in list_num_a]
    sorted(a_list, reverse=True)

target_num_asc = int(''.join(sorted(str(target_num))))

n = int(input())
x, y = map(int, input().split())
a = list(map(int, input().split()))

# 数値を一桁ずつ分割
num_a = str(n)
list_num_a = list(num_a)
a_list = [int(s) for s in list_num_a]

# 
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
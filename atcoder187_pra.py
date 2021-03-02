n = int(input())
x, y = map(int, input().split())
a = list(map(int, input().split()))

# 数値を一桁ずつ分割
num_a = str(n)
list_num_a = list(num_a)
a_list = [int(s) for s in list_num_a]

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




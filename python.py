#atcoder提出用フォーマット

n = int(input())
x, y = map(int, input().split())

# 横一列に数値が入るパターン
a = list(map(int, input().split()))

# 数値を一桁ずつ分割
num_a = str(n)
list_num_a = list(num_a)
a_list = [int(s) for s in list_num_a]

# 縦一列に条件の数値が入るパターン
ary = []
for i in range(n):
    x, y = map(int, input().split())
    ary.append((x, y))

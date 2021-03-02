#atcoder提出用フォーマット

n = int(input())
x, y = map(int, input().split())
a = list(map(int, input().split()))

# 数値を一桁ずつ分割
num_a = str(n)
list_num_a = list(num_a)
a_list = [int(s) for s in list_num_a]
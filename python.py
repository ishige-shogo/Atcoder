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

# 縦一列一文字バージョン
s = list(input() for i in range(n))

# 縦横に広がるバージョン:nは縦の個数
v = [list(map(int,input().split())) for i in range(n)]

# 注意：縦一列一文字バージョン(重複したものを排除してる)
s = set(input() for i in range(n))

#-------------------------------------
#よく使う表現

# (0,1)(0,2)(0,3)(1,2)(1,3)(2,3)...のように全てを調べる方法
for s in range(n):
    for t in list(range(s+1,n)):
        break #←これは不要

# 2,8,16進数
# →10進数
print(0b10) #2
print(0o10) #8
print(0x10) #16

#　10進数→
print(bin(10)) # 0b1010
print(oct(10)) # 0o12
print(hex(10)) # 0xa

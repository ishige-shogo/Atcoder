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

# 昇順降順
A = [2,4,1,3,5]
a = sorted(A) #1,2,3,4,5
a = sorted(A, reverse=True) #5,4,3,2,1


# 組み合わせの数：nCr
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result
    
#切り上げ・切り捨て
import math
print(math.ceil(5.5)) # 切り上げ
print(math.floor(5.5)) # 切り捨て


# 1~10までのリスト化
list(range(5)) #[0, 1, 2, 3, 4]
list(range(3, 8)) #[3, 4, 5, 6, 7]
list(range(5, 31, 5)) # [5, 10, 15, 20, 25, 30]
list(range(100, -1, -10)) # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]


# 0の配列作成
zero = [0] * 10 #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#リストに同一の要素があるか判定
def has_duplicates(seq):
    return len(seq) != len(set(seq))
    
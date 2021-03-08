# A問題
n = int(input())

if n % 2 == 0:
    print("White")
else:
    print("Black")

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

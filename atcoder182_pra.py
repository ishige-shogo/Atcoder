# A問題
A, B = map(int, input().split())
print(((2*A)+100)-B)

#--------------------------------------------------------
# B問題

# 数列の数
n = int(input())
# 数列
a = list(map(int, input().split()))

# 最大のgcd度を記録
gcd = 0
for i in range(2, (max(a)+1)):
    count = 0
    # 割り切れたらカウントしていく
    for s in a:
        if s % i == 0:
            count += 1
    # 記録されているgcd度より大きい場合、ansとgcdを更新
    if max(count, gcd) == count:
        ans = i
    gcd = max(count, gcd)

print(ans)

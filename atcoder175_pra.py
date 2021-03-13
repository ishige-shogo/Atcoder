# A問題

s = input()
ans = 0
count = 0
# Rが連続する回数を記録
for i in s:
    if i == "R":
        count += 1
    else:
        count = 0
    ans = max(ans, count)
print(ans)

#-----------------------------------------------------
# B問題

n = int(input())

a = list(map(int, input().split()))

ary = []
count = 0
for i in range(n):
    for s in range(i+1, n):
        for v in range(s+1, n):
            # 3辺がそれぞれ異なる値の場合のみ検証
            if a[i] != a[s] and a[i] != a[v] and a[s] != a[v]:
                ary.append(a[i])
                ary.append(a[s])
                ary.append(a[v])
                ary = sorted(ary)
                # 短い2辺の合計が最も長い1辺よりも大きい場合に三角形を作成できる
                if ary[0] + ary[1] > ary[2]:
                    count += 1
            ary = []
print(count)

#-----------------------------------------------------
# C問題

# 解法１：実行時間エラー
x, k, d = map(int, input().split())

for _ in range(k):
    if x >= 0:
        x -= d
    else:
        x += d

print(abs(x))

# 解法２(正解パターン)
x, k, d = map(int, input().split())

x, k, d = -3, 1, 1

if abs(x) - (k * d) >= 0:
    print(abs(x) - (k * d))
    exit()

k -= x//d
x -= (x//d) * d

if k % 2 == 0:
    print(x)
else:
    print(abs(x-d))

#----
x, k, d = map(int, input().split())

x, k, d = 13, 5, 3

if x - (k * d) > 0:
    print(x - (k * d))
    exit()

am = x//d
bm = x//d + 1

print(min(abs(x - (am * d)), abs(x - (am * d))))
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
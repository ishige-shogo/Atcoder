#------------------------------------------------------------

x, y = map(int, input().split())

# x,yの差が３より下の場合は逆転可能
if abs(x-y) < 3:
    print("Yes")
else:
    print("No")

#-------------------------------------------------------------

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
# お互いの配列の要素を掛け合い、合計していく
for i in range(n):
    sum += a[i] * b[i]

if sum == 0:
    print("Yes")
else:
    print("No")

#---------------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))
# Aの配列の要素を２つに分ける(仮に８つの要素の場合４:４にする)
a=list(zip(*[iter(A)]*int(2**N/2)))
# それぞれの最大の数値を比べ、小さいほうをsemとする
sem = min(max(a[0]),max(a[1]))
# semが準優勝の数値なので、その順番を求める
print(A.index(sem)+1)

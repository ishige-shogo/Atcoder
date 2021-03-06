# A問題

s = input()

if s[-1] == "s":
    word = s + "es"
else:
    word = s + "s"

print(word)

#------------------------------------------------------
# B問題

n = int(input())

# ぞろ目が出たらカウント。３回連続であればYESを出力し、終了。
count = 0
for i in range(n):
    x, y = map(int, input().split())
    if x == y:
        count += 1
    else:
        count = 0
    if count == 3:
        print("Yes")
        exit()
print("No")

#----------------------------------------------------------
# C問題

# A*B+C=Nとなる組み合わせ(ABCは正の整数)
n = int(input())
count = 0
# A,Bが決まればCは確定する。
# Aの範囲は[1 ~ (n-1)] (nまでにするとC=0となるから)
for i in range(1, n):
    m = int(n/i)
    # A*B=Nとならないように場合分け
    if m * i == n:
        count += m - 1
    else:
        count += m
print(count)
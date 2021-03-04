# A問題

a, b = map(int, input().split())
c, d = map(int, input().split())
print((a*d)-(b*c))

#-------------------------------------------------------
# B問題

# n, x = 問題数, 最初の持ち点
n, x = map(int, input().split())
s = str(input())

for i in range(n):
    # oの場合１点プラス
    if s[i] == "o":
        x += 1
    # xの場合、現在の点数が0点でない場合にのみマイナス１点
    elif s[i] == "x" and x != 0:
        x -= 1
print(x)

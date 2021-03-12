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
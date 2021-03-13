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

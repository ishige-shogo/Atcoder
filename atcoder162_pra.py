# A問題

n = [int(s) for s in list(str(int(input())))]

if 7 in n:
    print("Yes")
else:
    print("No")

#---------------------------------------------
# B問題

n = int(input())

ans = 0
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        ans += i
print(ans)


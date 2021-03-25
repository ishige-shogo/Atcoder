# A問題

k = int(input())
a, b = map(int, input().split())

for i in range(a,b+1):
    if i % k == 0:
        print("OK")
        exit()
print("NG")

#----------------------------------------------------
# B問題

from decimal import Decimal
x = int(input())

money = 100
ans = 0
while money < x:
    ans += 1
    # money = int(Decimal(money*1.01))だと失敗する
    money = money * 101 //100

print(ans)

from decimal import Decimal
i = "245673867548237383733920.9303725374845243748"

print(int(Decimal(i)))


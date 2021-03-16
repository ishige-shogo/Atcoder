# A問題
import math
n = int(input())

m = math.ceil(n / 1000)

print(m * 1000 - n)

#------------------------------------------------------
# B問題

n = int(input())

ac = 0
wa = 0
tle = 0
re = 0

for _ in range(n):
    s = input()
    if s == "AC":
        ac += 1
    elif s == "WA":
        wa += 1
    elif s == "TLE":
        tle += 1
    elif s == "RE":
        re += 1

print("AC x "+str(ac))
print("WA x "+str(wa))
print("TLE x "+str(tle))
print("RE x "+str(re))

#---------------------------------------------------------
# C問題

h, w, k = map(int, input().split())

c = [list(map(input().split())) for i in range(h)]






# 番外編(両替機)
n = 123456
money = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
rest = []
for coin in money:
    rest.append(n // coin)
    n %= coin
for (m, r) in zip(money, rest):
    print(str(m) + ":" + str(r))
    

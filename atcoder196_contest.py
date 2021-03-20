
a, b= map(int, input().split())
c, d = map(int, input().split())

print(b-c)


#-------------------------
import math
x = float(input())

print(int(x))

#---------------------------

n = int(input())



count = 0
for i in range(11, n+1):
    num = str(i)
    if len(num) % 2 == 0:
        m = len(num) // 2
        if num[:m] == num[m:]:
            count += 1
print(count)

#--------------------
n = int(input())

if n <= 10:
    print(0)
    exit()

ans = 0
count = 1
num = 11
while num <= n:
    ans += 1
    count += 1
    b = str(count)
    num = int(b + b)
print(ans)

#---------------------------------------

h, w, a, b = map(int, input().split())

if a == 0:
    print(1)
    exit()


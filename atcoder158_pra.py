# A問題

s = input()

if ("A" in s) and ("B" in s):
    print("Yes")
else:
    print("No")

#--------------------------------------------------
# B問題

n, a, b = map(int, input().split())

ball = a + b

cnt = n // ball

rest = n % ball

if a > rest:
    print(cnt * a + rest)
else:
    print(cnt * a + a)

#---------------------------------------------------
# C問題

a, b = map(int, input().split())

for i in range(1001):
    if ((i * 8)//100 == a) and ((i * 10)//100 == b):
        print(i)
        exit()
print(-1)


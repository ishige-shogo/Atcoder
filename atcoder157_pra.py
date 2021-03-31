# A問題
import math
n = int(input())

print(math.ceil(n/2))

# B問題

bingo = []
for _ in range(3):
    a,b,c = map(int, input().split())
    bingo.append(a)
    bingo.append(b)
    bingo.append(c)
print(bingo)

n = int(input())

for i in range(n):
    hit = int(input())
    for s in range(9):
        if bingo[s] == hit:
            bingo[s] = 0
    
if bingo[0] == 0 and bingo[1] == 0 and bingo[2] == 0:
    print("Yes")
elif bingo[3] == 0 and bingo[4] == 0 and bingo[5] == 0:
    print("Yes")
elif bingo[6] == 0 and bingo[7] == 0 and bingo[8] == 0:
    print("Yes")
elif bingo[0] == 0 and bingo[3] == 0 and bingo[6] == 0:
    print("Yes")
elif bingo[1] == 0 and bingo[4] == 0 and bingo[7] == 0:
    print("Yes")
elif bingo[2] == 0 and bingo[5] == 0 and bingo[8] == 0:
    print("Yes")
elif bingo[0] == 0 and bingo[4] == 0 and bingo[8] == 0:
    print("Yes")
elif bingo[2] == 0 and bingo[4] == 0 and bingo[5] == 0:
    print("Yes")
else:
    print("No")
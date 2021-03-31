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

#------------------------------------------------------
# D問題
import sys
from collections import deque

input = sys.stdin.readline

def main():
    s = input()
    ans = deque()
    for i in s:
        ans.append(i)
    q = int(input())
    reverse = False
    for _ in range(q):
        query = input().split()
        if query[0] == "1":
            reverse = not reverse
        else:
            if (query[1] == "1" and not reverse) or (query[1] == "1" and reverse):
                ans.appendleft(query[2])
            else:
                ans.append(query[2])
    ans = list(ans)
    if reverse:
        print(*ans[::-1], sep="")
    else:
        print(*ans, sep="")

if __name__ == '__main__':
    main()


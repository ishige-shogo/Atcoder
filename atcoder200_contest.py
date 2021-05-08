n = int(input())
n -= 1
print(n//100+1)


n, k = map(int, input().split())
def two(num):
    num /= 200
    return int(num)
def notwo(num):
    a = str(num)
    b = a + "200"
    c = int(float(b))
    return c
for _ in range(k):
    if n % 200 == 0:
        n = two(n)
    else:
        n = notwo(n)
print(n)


import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main(N,A):

    def num(x, y):
        if (x-y) % 200 == 0:
            return True
        else:
            return False

    ans = 0
    for i in range(N):
        for s in range(i+1, N):
            if num(A[i], A[s]):
                ans += 1
    return ans

N = int(readline())
A = np.array(list(map(int,readline().split())))

print(main(N,A))
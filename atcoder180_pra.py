# A問題

n, a, b = map(int, input().split())

print(n - a + b)

#----------------------------------------------
# B問題

n = int(input())

x = list(map(int, input().split()))

man = 0
yuk = 0
tyb = 0

for i in x:
    man += abs(i)

for s in x:
    yuk += s**2
yuk = yuk ** (1/2)

for v in x:
    tyb = max(tyb, abs(v))

print(man)
print(yuk)
print(tyb)

#-------------------------------------------------
# C問題

# 解法１：実行時間エラー
N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i)

# 解法２：実行時間エラー
import math

N = int(input())

n = math.ceil(N/2)

ary = []
for i in range(1, n+1):
    if N % i == 0:
        ary.append(i)
        ary.append(N//i)

ary_new = sorted(set(ary))

for s in ary_new:
    print(s)

#--

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N = int(input())

for i in make_divisors(N):
    print(i)
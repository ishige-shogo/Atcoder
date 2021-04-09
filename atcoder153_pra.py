# A問題
import math
H, A = map(int, input().split())
print(math.ceil(H/A))

# B問題

H, N = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) >= H:
    print("Yes")
else:
    print("No")


# C問題

n, k = map(int, input().split())
h = sorted(list(map(int, input().split())), reverse=True)
print(sum(h) - sum(h[:k]))

# D問題

import math
v = int(math.log(int(input()), 2))
print((2**(v+1))-1)

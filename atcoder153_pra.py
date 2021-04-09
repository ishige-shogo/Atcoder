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


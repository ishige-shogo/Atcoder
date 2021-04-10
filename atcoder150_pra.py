# A問題

k, x = map(int, input().split())

if x <= k*500:
    print("Yes")
else:
    print("No")

# B問題

n = int(input())
s = input()

ans = 0
for i in range(n-2):
    v = s[i] + s[i+1] + s[i+2]
    if v == "ABC":
        ans += 1

print(ans)

# C問題

import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

n_list = list(range(1, n+1))
N = list(itertools.permutations(n_list))

print(abs(N.index(p) - N.index(q)))
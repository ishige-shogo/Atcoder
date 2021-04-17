# A問題

a, b = map(int, input().split())

l = a - (2*b)

if l <= 0:
    print(0)
else:
    print(l)

# B問題

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans += (sum(a) - i) * i
print(ans//2)

#別解
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    for s in range(i+1, n):
        ans += a[i]*a[s]
print(ans)


# C問題

n = int(input())
s = input()

color = ""
ans = 0
for i in range(n):
    if color != s[i]:
        ans += 1
    color = s[i]
print(ans)

# D問題

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

n = int(input())
l = list(map(int,input().split()))

ans = []
for a in range(n):
    for b in range(a+1, n):
        for c in range(b+1, n):
            if (l[a] + l[b] > l[c]) and (l[b] + l[c] > l[a]) and (l[c] + l[a] > l[b]):
                ans.append([l[a], l[b], l[c]])

print(len(get_unique_list(ans)))

#---------

import bisect

n = int(input())
l = sorted(list(map(int,input().split())), reverse=True)

ans = 0
for a in range(n):
    for b in range(a+1, n):
        m = bisect.bisect_left(l, l[a]-l[b])
        ans += m - b + 1

print(ans)

import bisect
list1 = [1,2,3,4,5]
value1 = 3
print(bisect.bisect(list1, value1))



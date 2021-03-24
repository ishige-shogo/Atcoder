# A問題

s = input()

if s == "ABC":
    print("ARC")
else:
    print("ABC")

#------------------------------------------------------
# B問題

n, k = map(int, input().split())

ary = []
for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    ary += a

print(n - len(set(ary)))


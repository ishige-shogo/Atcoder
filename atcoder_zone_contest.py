
x, y = map(int, input().split())

s = input()
ans = 0
for i in range(len(s)-3):
    if s[i] == "Z" and s[i+1] == "O" and s[i+2] == "N" and s[i+3] == "e":
        ans += 1
print(ans)



n, d, h = map(int, input().split())

# x*(y-ans) == d*(h-ans)
# xy-xans = dh - dans
# dans-xans=dh-xy
# ans d-x = dh-xy

n, d, h = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    ans = ((d*h)-(x*y))/(d-x)

print(ans)

n, d, h = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    ans = (x*(10-y))/(d-x)
    ans = min(y-ans, 1000)

if ans <= 0:
    print(0)
else:
    print(ans)


n, d, h = map(int, input().split())

n, d, h = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    cnt = min((h-y)/(d-x), 10**7)

ans = cnt * d
if h-ans <= 0:
    print(0.0)
else:
    print(h-ans)


n, d, h = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    cnt = y - (((h-y)/(d-x))*x)
    ans = max(cnt,ans)
print(ans)
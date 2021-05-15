x, y, z = map(int, input().split())

a = sorted(list(map(int, input().split())))

if a[0]-a[1] == a[1]-a[2]:
    print("Yes")
else:
    print("No")


n = int(input())
a = []
b = []
for _ in range(n):
    s, t = input().split()
    t = int(t)
    a.append(s)
    b.append(t)
c = sorted(b, reverse=True)
print(a[b.index(c[1])])



s = input()
cnt = 0
for i in range(10000):
    flag = True
    a = '{0:04}'.format(i)
    for x in range(10):
        if s[x] == "o":
            if str(x) not in a:
                flag = False
        elif s[x] == "x":
            if str(x) in a:
                flag = False
    if flag:
        cnt += 1

print(cnt)


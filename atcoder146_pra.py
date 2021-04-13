# A問題

s = input()
week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
print(7 - week.index(s))

# B問題

n = int(input())
s = input()

ans = ""
for i in s:
    m = ord(i) + n
    if m > 90:
        ans += chr(64 + (m - 90))
    else:
        ans += chr(ord(i) + n)

print(ans)


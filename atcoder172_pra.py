# A問題

a = int(input())

b = a**2
c = a**3

print(a + b + c)

#--------------------------------------------------------
# B問題
s = input()
t = input()

n = len(s)

ans = 0
for i in range(n):
    if s[i] != t[i]:
        ans += 1

print(ans)
        
#--------------------------------------------
# C問題



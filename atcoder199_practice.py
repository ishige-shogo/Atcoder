

a,b,c = map(int, input().split())

if (a**2) + (b**2) < c**2:
    print("Yes")
else:
    print("No")


#-------------------------------

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = min(b)-max(a)+1

if ans >= 0:
    print(ans)
else:
    print(0)


#------------------------

n = int(input())
s = list(input())
q = int(input())

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        c = s[a-1]
        d = s[b-1]
        s[b-1] = c
        s[a-1] = d
    else:
        x = s[:n]
        y = s[n:]
        s = y + x
    
print(s)



def t1(st,a,b):
    st[a], st[b] = st[b], st[a]
    return st

def t2(st,n):
    st = st[n:] + st[:n]
    return st

n = int(input())
s = list(input())
q = int(input())
r = [list(map(int,input().split())) for i in range(q)]

for i in r:
    if i[0] == 1:
        s = t1(s, i[1]-1, i[2]-1)
    else:
        s = t2(s, n)
print(''.join(s))





n = int(input())
s = input()
q = int(input())

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        s[b-1], s[a-1] = s[a-1], s[b-1]
    else:
        x, y = s[n:], s[:n]
        s = y + x
    
print(''.join(s))


import sys
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main(N,S,Q,R):
    def t1(st,a,b):
        st[a], st[b] = st[b], st[a]
        return st

    def t2(st,n):
        st = st[n:] + st[:n]
        return st

    for i in R:
        if i[0] == 1:
            s = t1(s, i[1]-1, i[2]-1)
        else:
            s = t2(s, n)

    return s

n = int(input())
s = list(input())
q = int(input())
r = [list(map(int,input().split())) for i in range(q)]

print(main(n,s,q,r))




n = int(input())
s = input()
q = int(input())




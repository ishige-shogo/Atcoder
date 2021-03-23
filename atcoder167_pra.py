# A問題
s_list = [str(s) for s in list(str(input()))]
t_list = [str(s) for s in list(str(input()))]

t_list = t_list.pop(-1)

if t_list == s_list:
    print("Yes")
else:
    print("No")
#-------
s = input()
t = input()

m = len(s)

if s == t[:m]:
    print("Yes")
else:
    print("No")


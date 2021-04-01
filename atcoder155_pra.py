# A問題

a, b, c = map(int, input().split())

if a == b and a == c:
    print("No")
elif a == b:
    print("Yes")
elif b == c:
    print("Yes")
elif a == c:
    print("Yes")
else:
    print("No")
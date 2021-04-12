# A問題

a = int(input())
b = int(input())

x = [1,2,3]

y = [a, b]

print(list(set(x) - set(y))[0])


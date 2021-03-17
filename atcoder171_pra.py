# C問題

n = int(input())

ary = []
while True:
    ary.append(n % 26)
    n = n // 26
    if n < 26:
        ary.append(n)
        break

alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

ans = ""

for i in ary:
    st = alph[i]
    ans += st

print(ans)
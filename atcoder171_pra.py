# C問題

n = int(input())

ary = []
while n > 0:
    n -= 1
    ary.append(n % 26)
    n = n // 26
    
alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

ans = ""

for i in reversed(ary):
    st = alph[i]
    ans += st

print(ans)

def main():
    N = int(input())
    result = []
 
    while N > 0:
        N -= 1
        result.append(N % 26)
        N //= 26
    
    print(''.join([chr(ord('a')+n) for n in result[::-1]]))
 
main()
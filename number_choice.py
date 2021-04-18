
import random
random.randint(1,9)

ans = []
for _ in range(3):
    s = random.randint(1,9)
    ans.append(s)

count = 1

while True:
    print("数字を当ててください")
    x_list = [int(s) for s in list(str(int(input())))]
    if ans == x_list:
        print(str(count) + "回目に当てました")
        exit()
    count += 1
    hit, blow = 0, 0
    for i in range(3):
        if x_list[i] == ans[i]:
            hit += 1
        elif x_list[i] in ans:
            blow += 1
    print("HIT:" + str(hit) + "、BLOW:" + str(blow))



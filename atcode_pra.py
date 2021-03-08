sum = 0
for i in range(1, 65):
    sum += i**4 
print(sum)

#----------------------------------------------
n = 1234567890

m = 1
ary = []
while m <= 5000000:
    if n % m == 0:
        ary.append(m)
    m += 1
print(sum(ary))

#------------------------------------------------

m = 1
ans = 0
while True:
    ans += 1 / m
    if ans > 8:
        print(m)
        exit()
    m += 1
    
#-------------------------------------------------

ary = []
for i in range(1, 30001):
    num_a = str(i)
    list_num_a = list(num_a)
    a_list = [int(s) for s in list_num_a]
    if (i % 3 == 0) or (3 in a_list):
        ary.append(i)
print(sum(ary))

#-----------------------------------------------------

def num(n):
    num_a = str(n)
    list_num_a = list(num_a)
    a_list = [int(s) for s in list_num_a]
    ans = 1
    for i in a_list:
        ans *= i
    if len(str(ans))==1:
        return 1
    num_a = str(ans)
    list_num_a = list(num_a)
    a_list = [int(s) for s in list_num_a]
    ans = 1
    for i in a_list:
        ans *= i
    if len(str(ans))==1:
        return 2
    num_a = str(ans)
    list_num_a = list(num_a)
    a_list = [int(s) for s in list_num_a]
    ans = 1
    for i in a_list:
        ans *= i
    if len(str(ans))==1:
        return 3
    num_a = str(ans)
    list_num_a = list(num_a)
    a_list = [int(s) for s in list_num_a]
    ans = 1
    for i in a_list:
        ans *= i
    if len(str(ans))==1:
        return 4
    num_a = str(ans)
    list_num_a = list(num_a)
    a_list = [int(s) for s in list_num_a]
    ans = 1
    for i in a_list:
        ans *= i
    if len(str(ans))==1:
        return 5
    else:
        return 0

ary =[]
for v in range(1, 1000001):
    if num(v) == 5:
        ary.append(v)

print(len(ary))

#---------------------------------------------------------
#成功バージョン

a = [31, 28, 31, 30, 31, 30, 31, 31, 30 ,31, 30 ,31]
b = [31, 29, 31, 30, 31, 30, 31, 31, 30 ,31, 30 ,31]

count = 0
m = 3
day = 13
while True:
    if m % 4 == 0:
        for i in b:
            day += i
            if day % 7 == 5:
                count += 1
    elif m % 4 != 0:
        for s in a:
            day += s
            if day % 7 == 5:
                count += 1
    if count == 666:
        break
    m += 1

p = day // (365*3+366)

true_day = day - (365*3+366) * p

true_year = p * 4 + 2019

print(true_day, true_year)
#答え(2407年1月13日)


# 失敗バージョン
a=[13,44,72,103,133,164,194,225,256,286,317,347]
b=[13,44,73,104,134,165,195,226,257,287,318,348]


count = 0
m = 3
day = 0
while True:
    if m % 4 == 0:
        for i in b:
            day += i
            if day % 7 == 5:
                count += 1
    elif m % 4 != 0:
        for s in a:
            day += s
            if day % 7 == 5:
                count += 1
    if count == 666:
        print(day)
        exit()
    m += 1


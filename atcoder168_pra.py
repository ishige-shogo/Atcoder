# A問題

n = int(input())

num_a = str(n)
list_num_a = list(num_a)
a_list = [int(s) for s in list_num_a]

if a_list[-1] == 3:
    print("bon")
elif (a_list[-1] == 0) or(a_list[-1] == 1) or(a_list[-1] == 6) or(a_list[-1] == 8):
    print("pon")
else:
    print("hon")

#-----------------------------------------------------


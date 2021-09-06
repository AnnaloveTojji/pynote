# #bj remainder
n_list = []
for i in range(10):
    n = int(input())
    n_list.append(n%42)
x_list = []
for i in n_list:
    x = n_list.count(i)
    x_list.append(x)
res = 10
for i in x_list:
    if i > 1:
        res = res - 1
print(res)


## method 2
# n_list = []
# for i in range(10):
#     n = int(input())
#     n_list.append(n%42)
# s = set(n_list)
# l = list(s)
# print(len(l))
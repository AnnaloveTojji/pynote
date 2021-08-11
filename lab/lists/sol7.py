# 백준 8958: OX 퀴즈


n = int(input())

for i in range(n):
    cnt = 0
    x = input()
    o_list = x.split('X')
    for j in o_list:
        for k in range(len(j)+1):
            cnt += k
    print(cnt)
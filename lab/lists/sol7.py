# 백준 8958: OX 퀴즈

n = int(input())

for i in range(n):
    a = input()
    score = 0
    res = 0
    for j in a:
        if j == 'O':
            score += 1
        else:
            score = 0
        res += score
    print(res)
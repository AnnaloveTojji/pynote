# bj2231 분해합
n = int(input())
for i in range(n):
    num_str = str(i)
    for j in num_str:
        sum += int(j)
    if sum == n:
        print(i)
        break 
    
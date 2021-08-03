# 백준 1110: 더하기싸이클

n = int(input())
temp = n  
cnt = 0
while True:
    sum = (temp // 10) + (temp % 10)  
    new_num = ((temp % 10) * 10) + (sum % 10) 
    cnt += 1  
    if new_num == n :
        break
    num = new_num 
print(cnt)
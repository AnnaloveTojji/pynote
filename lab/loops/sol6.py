# 백준 1110: 더하기싸이클

n = int(input())
init = n  
cnt = 0
while True:
    sum = (init // 10) + (init % 10)  
    temp = ((init % 10) * 10) + (sum % 10) 
    cnt += 1  
    if temp == n :
        break
    init = temp 
print(cnt)

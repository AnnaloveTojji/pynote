# 자릿수더하기
def sol(n):    
    answer = 0 
    while n > 0:
        answer += n%10
        n=n/10
# publy -1
# 주식 차익 발생까지의 최소 날
def solution(price):
    size = len(price)
    answer = [-1] * size
    
    for i in range(size):
        for j in range(i+1,size):
            if price[i] < price[j]:
                answer[i] = abs(i-j)
                break
    
    return answer
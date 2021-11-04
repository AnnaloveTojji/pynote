# 더맵게 -heap
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # min heap
    while True:
        min1 = heapq.heappop(scoville) # pop min value
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + 2 * min2
        heapq.heappush(scoville, new_scoville) # insert element 
        answer += 1
    return answer
    

print(solution([1, 2, 3, 9, 10, 12],7)) #2

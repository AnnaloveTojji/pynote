#heap 더맵게
	def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville) #list to heapq
    
    while scoville[0] < K: #가장 작은 수가 기준보다 낮다면 계속
        if len(scoville)>1:
            answer += 1
            first = heapq.heappop(scoville) 
            second = heapq.heappop(scoville) 
            heapq.heappush(scoville, first + second *2)
        else:
            return -1
    return answer
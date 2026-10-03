import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    if scoville[0] >= K:
        return 0
    while len(scoville) >= 2:
        first, second = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, first + (second * 2))
        answer += 1
        if scoville[0] >= K:
            return answer
    return -1
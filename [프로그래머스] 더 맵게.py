#시간 초과 풀이
def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    while len(scoville)>=2 and scoville[0] <K:
        min1,min2 = scoville[:2]
        scoville = scoville[2:]
        scoville.append(min1+min2*2)
        scoville.sort() #sort를 while문 안에서 계속 반복하느라 시간초과가 생긴다.
        answer+=1
    if scoville[0] < K:
        return -1
    return answer

#heapq를 이용하면 시간복잡도를 낮출 수 있다.
#가지고 있는 요소를 넣거나 빼줄때마다 자동으로 정렬이 되기 때문.
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville)>=2 and scoville[0] <K:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1+min2*2)
        answer+=1
    if scoville[0] < K:
        return -1
    return answer
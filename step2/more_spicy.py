#first code 
# repeated sorted Method 
def solution(scoville, K):
    answer = 0
    s_v = scoville[:]
    while len(s_v) :
        s_v = sorted(s_v, reverse =True)
        a = s_v.pop()
        if a < K :
            if len(s_v) == 0 : #더이상 값이 없을 때
                return -1
            b = s_v.pop()
            c = a + (2*b)
            answer += 1
            s_v.append(c)
        else :
            return answer
    
    
    return answer
  
  # test success 
  # but, time error 
  
  # other code
  
  def solution(scoville, K):
    answer = 0
    s_v = sorted(scoville, reverse =True)
    check = []
    if s_v[-1] > K: #초기값이 다 K보다 클때 
        return answer
    check.append(s_v.pop())
    while len(check):
        check.append(s_v.pop())
        food_s = min(check) + (max(check)*2)  
        check.clear()
        answer += 1
        if food_s < K : # food_s 가  last 보다 클수도 있음
            if len(s_v) == 0:
                return -1
            if food_s > s_v[-1]:
                    last =s_v.pop()
                    check.append(last)
                    s_v.append(food_s)
                    s_v = sorted(s_v, reverse =True) #삽입후 다시 정리
            else: #food_s가 제일 작을 때
                check.append(food_s)

        else :  #  food_s이 K 보다 크거나 같을때
            if len(s_v) == 0 :
                return answer  #마지막 값이 K 보다 큼
            else:
                last = s_v.pop()
                if last >= K :
                    return answer #모든 수가 K 보다 크거나 같음
                else :
                    check.append(last)
                    s_v.append(food_s)
                    s_v = sorted(s_v, reverse =True) #삽입후 다시 정리

    return -1  # 계산을 거쳐도 K 보다 
  
  
  # but, Using repeated sorted_Method too
  # I got to know heap_Function
  
  # so next code
  import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i) //최소 힙
    
    while True:
        a = heapq.heappop(heap)
        if a < K:
            if len(heap) == 0 :
                answer = -1
                break
            b = heapq.heappop(heap)
            c = a + (2*b)
            answer += 1
            heapq.heappush(heap, c) //다시 넣기
        else : // 최소값이 K랑 같거나 클때 
            break
    
    return answer
  
  #similar to first code 
  #success

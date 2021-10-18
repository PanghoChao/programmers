#first code
def solution(stones, k):
    a = sum(stones)/len(stones)  // 나머지는 다 버림
    for i, s in enumerate(stones):
         stones[i] = s - a
    answer = a
    while True:
        for j in range(len(stones)): //완전 탐색
            if stones[j] <= 0 and j+k < len(stones):
                cnt = k
                for b in range(k):
                    if stones[j+b] <= 0 :
                        cnt -= 1
                if cnt <=0:
                    return answer
        answer += 1
        for i, s in enumerate(stones):
            stones[i] = s - 1
            
           
#Also, Error

## second code

def solution(stones, k):
    answer = 0
    while True:
        answer += 1
        for i, s in enumerate(stones):
            stones[i] = s - 1
            
        for j in range(len(stones)): 
            if stones[j] <= 0 and j+k < len(stones):
                cnt = k
                for b in range(k):
                    if stones[j+b] <= 0 :
                        cnt -= 1
                if cnt <=0:
                    return answer

# little Error 
# just i missing '=', j+k < len(stone)

def solution(stones, k):
    answer = 0
    while True:

        for j in range(len(stones)): 
            if stones[j] <= 0 and j+k <= len(stones):  //무한루프 돌지 않게 k길이를 고쳐주고
                cnt = k
                for b in range(k):
                    if stones[j+b] <= 0 :
                        cnt -= 1
                if cnt <=0:
                    return answer
        answer += 1                          // 값을 빼는걸 뒤에다 배치해주면
        for i, s in enumerate(stones):
            stones[i] = s - 1

#but time test Error 
# so, i used Binary Searching


# final code


  def solution(stones, k):
    answer = 0
    left = 1 
    right = max(stones)

    while left <= right :
        cnt = 0
        mid = (left+ right)//2 
        for stone in stones:
            if stone -mid <= 0:
                cnt += 1
            else:
                cnt = 0   
            if cnt >= k :
                break
        if cnt >=k:      
            answer = mid
            right = mid-1
        else :
            
            left = mid + 1 
    return answer
  

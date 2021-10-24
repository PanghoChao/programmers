#예상시나리오

'''
n개의 자연수로 합이 s 가 되는것중에 
n개의 자연수를 각각 곱한것이 최대가 되려면  s를 n으로 나눈값이 mid 값이라고 한다면
mid값에서 가까울수록 최대가된다 .

1. mid 값을 구하고 
2. s 에서 빼주면서 하나씩 추가 (n번 반복)
3. 나머지값 추가
'''

#first code
def solution(n, s):
    answer = []
    if s < n :
        return [-1]
    
    mid =  round(s / n)
    rest = s
    for _ in range(n): #n번 수행
        
        if rest >= mid :
            answer.append(mid)
        if rest < mid:
            if rest < 0 :
                answer.append(-1)
                break
            if rest > 0 :
                answer.append(rest)
        rest = rest - mid
        
    return answer
  
  #ERROR
  
  
# 문제점파악
'''
1.mid*n이 s보다 작을 때에는 에러가 나온다. 
2.조건문이 점점많아지고, s =14 , n= 4인경우 4,4,4,2 가 나온다 .
=> 4,4,3,3 이 최고의값이여야하고
3. 또한 answer값이 작은수 부터 나와야한다. 

결론: 조잡하다.
'''


#second code
def solution(n, s):
    answer = []
    if s < n :
        return [-1]
    
    mid =  s // n
    if s == (mid*n):
        for _ in range(n) :
            answer.append(mid)
        return answer
    if s > (mid *n):
        rest = s - (mid *n)
        for i in range(n) : #n 번 반복
            if i  >  (n-1) - rest :
                answer.append(mid +1)
            else: #rest가 0이면
                answer.append(mid)

    return answer
  
# success

#문제이해
https://blog.naver.com/sobrightlf/222555137445

  
#code

def solution(n, left, right):
    answer = []
    m1 = left //n +1
    k1 = left % n  
    
    m2 = right //n +1
    k2 = right % n 
    
    
    for i in range(m1, m2+1) :
        for idx in range(n):
            if i == m1 and idx< k1  : 
                continue
            if i > idx:
                answer.append(i)
            if i <= idx :
                answer.append(idx+1)
            if i == m2 and idx == k2 :
                break


    
    return answer
  
  
# best code
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        anwer.append(max(i//n, i%n)+ 1)
    return answer

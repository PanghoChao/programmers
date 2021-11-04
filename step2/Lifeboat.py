#문제이해
https://blog.naver.com/sobrightlf/222557506489
  
#code
def solution(people, limit):
    people.sort()
    boat_cnt = 0
    mn_idx = 0
    mx_idx = len(people) - 1
    
    while mn_idx <= mx_idx:
        boat_cnt += 1
        if people[mx_idx] + people[mn_idx] <= limit :
            mn_idx += 1
        mx_idx -= 1
    
                    
                
    return boat_cnt
  #인덱스로 처리해줘야 빠르다.

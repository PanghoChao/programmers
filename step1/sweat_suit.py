## Difficult Problem
## score +8  if solove it


## first code

def solution(n, lost, reserve):
    answer = 0
    while reserve: #reserve 다 확인 할 때까지
        r_elem = reserve.pop()
        if (r_elem + 1) in lost:   
            lost.remove(r_elem + 1) 
            continue                #빌려줬으면 다음으로
        if r_elem in lost:
            lost.remove(r_elem)
            continue
        if (r_elem - 1) in lost:
            lost.remove(r_elem - 1)
            continue
        
    answer = n - len(lost) #전체에서 빌리지못한 학생수를 뺀다.
    
    
    return answer
  
 # error



## second code
    reserve.sort() #정렬이 안되어있을경우를 추가
## add a codeline
## but, error 
## 조건문 추가 필요

### third code

def solution(n, lost, reserve):
    answer = 0

########################     add code     ##########################
    not_self_reserve = reserve
    

    for uriform_self in reserve:
        if uriform_self in lost: #여벌이 있는데 도난당한경우 
            lost.remove(uriform_self)
            not_self_reserve.remove(uriform_self)
####################################################################

    not_self_reserve.sort() #정렬이 안되어있을경우를 
    
    
    while not_self_reserve: #reserve 다 확인 할 때까지
        r_elem = not_self_reserve.pop()
        if (r_elem + 1) in lost:   
            lost.remove(r_elem + 1) 
            continue                #빌려줬으면 다음으로

        if (r_elem - 1) in lost:
            lost.remove(r_elem - 1)
            continue
        
    answer = n - len(lost) #전체에서 빌리지못한 학생수를 뺀다.
    
    
    return answer

# object error
# python is object language

    not_self_reserve = reserve.copy()
    not_self_reserve = reserve[:]
    not_self_reserve = []+reserve
    not_self_reserve = list(reserve)




#### 4th code

def solution(n, lost, reserve):
    answer = 0
    not_self_reserve = reserve.copy()
    
    
    for uriform_self in reserve:
        if uriform_self in lost: #여벌이 있는데 도난당한경우 
            lost.remove(uriform_self)
            not_self_reserve.remove(uriform_self)

            
    not_self_reserve.sort() #정렬이 안되어있을경우를 
    
    
    while not_self_reserve: #reserve 다 확인 할 때까지
        r_elem = not_self_reserve.pop()
        if (r_elem + 1) in lost:   
            lost.remove(r_elem + 1) 
            continue                #빌려줬으면 다음으로

        if (r_elem - 1) in lost:
            lost.remove(r_elem - 1)
            continue
        
    answer = n - len(lost) #전체에서 빌리지못한 학생수를 뺀다.
    
    
    return answer

  # success


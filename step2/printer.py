# first code #

def solution(priorities, location):
    
    answer = 0
    f = priorities.index(max(priorities))
    if f > location :
        answer = len(priorities) + location - f + 1
    else:
        answer= location - f +1
        
    return answer
  
# test code pass
# submission error
# misunderstood the question



## second code  #

def solution(priorities, location):
    cnt = 0
    target= priorities[location]
    while True:
        l = len(priorities)
        if max(priorities) > target:
            f = priorities.index(max(priorities))
            if f > location :
                location = l + location - f
                print(f)
            else:
                location -= f
            priorities.remove(max(priorities))           
            cnt += 1
        else:
            check = priorities[:location]
            cnt += check.count(target)
            #pprint.pprint(locals())
            break
    return cnt

# location calculation mistake.
# len() keeps changing
# so, used deque and itertools 

### third code #

from collections import deque
import itertools
def solution(priorities, location):
    cnt = 0
    deq = deque(priorities)
    target = priorities[location]

    while True:
        if location < 0 :
            location += len(deq) 
        mx= max(deq) 
        if target < mx :
            ext = deq.popleft()
            location -= 1 
            if mx > ext :
                deq.append(ext)
            else :
                cnt += 1
        else: #target = mx
            print(deq, location)
            cnt += list(itertools.islice(deq,0, location+1)).count(target)
         
            break 

        
    return cnt

#success

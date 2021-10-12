
#first code

def solution(participant, completion):
    answer= ''
    answer = answer.join(x for x in participant if x not in completion)

    return answer
  
  
# error
# participant에 있는 값은 값도 삭제 처리됨

# second code

def solution(participant, completion):
    answer= ''
    for x in completion:
        participant.remove(x)
    
    answer = answer.join(participant)

    return answer
  
#runTime error
#하나씩 제거하여 남은 값하나를 리턴하는 방식이나
#시간이 너무 오래 걸림

#third code
from collections import defaultdict

def solution(participant, completion):
    answer= ''
    
    dict_name = defaultdict(int)
    
    
    for p_name in participant :
        dict_name[p_name] += 1
        
    for c_name in completion:
        dict_name[c_name] -= 1
        
        if dict_name[c_name] == 0 :
            del dict_name[c_name]  
    
    answer = "".join(dict_name.keys())

    return answer
  
  
 #success 
# dict를 활용하여 결과물 도출

# bonus  code 
# 문제를 통과하고 다른사람이 풀이하는걸 보고 알게된 코드 
# Counter 객체는 서로 연산이 가능하다!


import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]




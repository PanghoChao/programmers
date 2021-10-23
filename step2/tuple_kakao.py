# 문제이해
# https://blog.naver.com/sobrightlf/222546029813

# 예상시나리오
'''
1. 먼저 문자열에서 "{} " 제거해주고 
2. "," 를 중심으로 리스트로 전환한 다음  
3. answer에 중복되지않게 추가해준다. 
'''


# first code
def solution(s : str):
    answer = []
    
    s2= s.replace("{", "")
    s3= s2.replace("}", "")
    s4= s3.split(",") 
    # print(s4)
    for i in s4 : 
        if i not in answer:
            answer.append(i)
    
    return answer
  
# but, error
#문제점 파악 
'''
결과값에 들어가야하는 순서가 {}의 길이가 짧은 순서 였던 것이다. 
"{{1,2,3},{2,1},{1,2,4,3},{2}}"
{2} -> {2,1} -> {1,2,3} -> {1,2,3,4}
result = {2,1,3,4}
  '''

# second code
def solution(s : str):
    answer = []
    tupl =[]
    ss= s.replace("{", "", 2)
    sss= ss.replace("}", "")
    
    s4= sss.split("{")
    for i in s4 :
        j = i.strip(",").split(",")
        tupl.append(j)
        
    tupl.sort(key = lambda x :len(x))
    
    for key in tupl:
        for value in key :
            v= int(value)
            if v not in answer:
                answer.append(v) 

    
    return answer

#success

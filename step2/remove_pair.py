#문제이해
# https://blog.naver.com/sobrightlf/222543572526

# 예상 시나리오
'''

1. 문자열(s)을 하나씩(i) 보고 다른 배열(check)에 저장해준다.
2. 다른 배열(check)과 문자열(s)에서 뺀 하나를 비교(if c == i)한다.
3. 같으면 제거해주고, 다르면 다른배열(check)에 다시 넣어준다.
4. 마지막에 다른 배열(check)이 비어있으면 통과!

'''

#first code
def solution(s):
    check = []
    
    for i in s:
        if len(check) == 0 :
            check.append(i)
            continue
        
        c = check.pop()
        if c == i:
            continue
        check.append(c)
        check.append(i)
    
    if check : #check 안에 있으면
        return 0

    return 1
  
  #success

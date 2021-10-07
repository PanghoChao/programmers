#등비수열 문제 
#그리고 각 자리당 공식은 
'''
마지막 자리 =  +1 (A = 1, E= 2, I=3 ,O=4, U=5)

네번째 자리 = (마지막자리 x 5)  + 1

세번째 자리 = (네번째자리 x 5)  + 1

두번째 자리 = (세번째자리 x 5)  + 1

첫번째 자리 = (두번째자리 x 5)  + 1

첫번째 자리 공식  
'''

##규칙을 찾아 별도 배열을 만들어 계산##


def solution(word):
    words = ["A","E","I","O","U"]
    squence_num = [781, 156, 31, 6, 1]
    answer = 0
    for word_idx, alph in enumerate(word):
        answer = answer + words.index(alph) * squence_num[word_idx] + 1
        
    return answer
  
  
### 재귀적 표현으로 계산 ###
def rowel_dict(n:int)->int:
    if n == 1  :
        return 1
    n -= 1
    squence_num = rowel_dict(n) * 5 + 1
    return squence_num
    
def solution(word):
    words = ["A","E","I","O","U"]
    answer = 0
    for idx, alph in enumerate(word):
        answer += rowel_dict(5-idx) * words.index(alph) + 1
    
        
    return answer



#문제 사이트 
# https://programmers.co.kr/learn/courses/30/lessons/84512

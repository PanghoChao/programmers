#문제이해
url = https://blog.naver.com/sobrightlf/222554731086
#code
def solution(citations):
    answer = len(citations)
    c = sorted(citations, reverse= True)
    for i, h in enumerate(c):
        if i + 1 == h:
            answer = h
            break
        if i + 1 > h : 
            answer = i
            break
        
    return answer

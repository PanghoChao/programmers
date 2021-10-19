# 문제 이해하기

# skill 안에 있는 문자는 순서대로 나와야 하지만, 
# skill 외에 있는 문자는 순서와 관계없이 가능합니다.
# 그랬을때 skill_trees 중 가능한 갯수를 찾는 문제입니다.

# 참고링크 https://programmers.co.kr/learn/courses/30/lessons/49993#fn1

# expected scenario

'''
skill에 있는 문자열을 문자 단위로 나누고 skill 트리에 있는 애들도 나눕니다. 

여기서 중요한것은 skill의 문자열과 같이 문자들이 순서가 잘 배치되었냐이니까 

skill_trees 에서 =>각 요소별로 skill 문자열만 뽑습니다.  if skill_trees_elem in skill_c

그리고 따로 뽑은 문자열을 리스트에 넣어줍니다. 
'''




# first code 

def solution(skill, skill_trees):
    cnt = 0  //return 할 값
    skill_s =[] //문자열을 배열로 바꿀갑
    
    for s in skill:
        skill_s.append(s)
    
    for s_tree in skill_trees : 
        check = []
        for s_char in s_tree:
            if s_char in skill_s :
                check.append(s_char)
        print(skill_s, check)        
        if skill_s[:len(check)] == check:
            cnt += 1
        
        
    return cnt
  
  
  # success 
  
# bonus code
# 굳이 리스트로 바꾸지않고 문자열로 풀이

def solution(skill, skill_trees):
    cnt = 0
    skill_s =[]
    
    #for s in skill:
    #   skill_s.append(s)
    
    for s_tree in skill_trees : 
        check = ""
        for s_char in s_tree:
            if s_char in skill:
                check += "".join(s_char)
        print(skill, check)        
        if skill[:len(check)] == check:
            cnt += 1
        
        
    return cnt

#문제이해 
# 당첨에서 제외되어야 할 아이디 목록의 경우의 수를 찾는 것! 
# 참고 링크 https://blog.naver.com/sobrightlf/222540651582



# 예상 시나리오 
'''
기본적으로 큰틀은 문자열 비교 문제이다.
banned_id 와 같은 값이 있으면  +1 씩 해주고, 
1나 뿐이 값은 무시해줘도 되고, 2개 부터는 dict 으로 정렬하여 어쩌구 저쩌구 
시나리오 짜기도 쉽지않았다.

1. banned_id 문자열 비교하여, combination으로 정리하여 저장한다.
2. 그 나온 combinations를 하나하나 비교한다 // *은 통과시키고 나머지는 비교한다.
3. 비교하여 아닌값은 버리고, 새로운배열에 넣는다. 
4. 새로운 배열의 길이를 재면 경우의수가 나온다.

'''

#first code
from itertools import combinations

def solution(user_id, banned_id):
    user_combination = list(combinations(user_id,len(banned_id))) #콤비네이션은 튜플로 저장됨
    banned_Set = []
    # 먼저 문자열 비교로 dict 만들기 

    for users in user_combination:
        # 하나의 튜플과 비교 시작

        if check(users, banned_id):
            if users not in banned_Set:
                banned_Set.append(users)
        else:
            continue # 다음 튜플로 넘어가기
    print(banned_Set)
    return len(banned_Set)


def check(users,banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False # 현재 튜플 불일치
    
    return True #일치하면 True 리턴

  
  
#Error 
#so, debug 
#combinations remove overlap
#so, permutations used


# second code

from itertools import permutations  #순열로 바꿈
def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id,len(banned_id))) 
    banned_Set = []
    # 먼저 문자열 비교로 dict 만들기 

    for users in user_permutation:
        # 하나의 튜플과 비교 시작

        if not check(users, banned_id):
            continue # 다음 튜플 가져오기
        else:
            users =set(users)  # 순열이기에 중첩 제거 
            if users not in banned_Set:
                banned_Set.append(users)
    print(banned_Set)
    return len(banned_Set)


def check(users,banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False # 현재 튜플 불일치
    
    return True

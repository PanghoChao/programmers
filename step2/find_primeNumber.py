#문제이해
https://blog.naver.com/sobrightlf/222552869759
  
# code

from itertools import permutations

def prime_number(check)-> bool:
    if check <= 1:
        return False

    for j in range(2, int(check**(1/2))+1) :
        if check % j == 0: #약수가 있으면 소수아님
            return False
    return True        # 약수가 없다면 소수임



def solution(numbers):
    answer = 0
    idx= []
    k = len(numbers)
    for n in range(1,k+1):  # 조합 길이 
        l = list(permutations(numbers, n))
        for nums in l :
            a = ""
            for number in nums: #튜플안에있는 문자열 합치기
                a += number
            check = int(a)#문자열 숫자로 전환
            if prime_number(check) and check not in idx :# 소수인지 확인해야된다. 
                idx.append(check)  #중복 방지
                answer += 1   #소수이면 +1  
                                
    return answer



print(solution("17"))   
print(solution("011"))   

#success

def solution(left, right):
    answer = 0
    for num in range(left, right +1):
        div_cnt = 1           //자기자신이 약수
        
        for div_num in range(1, num//2+1) :
            if num % div_num == 0:     //약수 조건
                div_cnt += 1
              
        if div_cnt % 2 == 0 : //약수갯수가 짝수
            answer += num
        else :                //약수 갯수가 홀수
            answer -= num
        print(div_cnt)
    return answer

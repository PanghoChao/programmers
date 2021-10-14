#### first code ####

def solution(answers):
    answer = []
    number1 = [1,2,3,4,5] //1번 수포자
    number2 = [2,1,2,3,2,4,2,5] //2번 수포자
    number3 = [3,3,1,1,2,2,4,4,5,5]//3번 수포자
    cnt1,cnt2,cnt3 = 0, 0 ,0
    
    
    for idx, ans in enumerate(answers): //한번의 탐색으로 1번, 2번,3번을 다 찾을수 있게 만들고
        if ans == number1[idx%5] : 
            cnt1 +=1                     //1번이 맞힌 문제수
        if ans == number2[idx%8] :
            cnt2 +=1                    //2번이 맞힌 문제수
        if ans == number3[idx%10] :
            cnt3 +=1                    //3번이 맞힌 문제수
    
    m = max(cnt1, cnt2, cnt3) 
    if m == cnt1:
        answer.append(1)
    if m == cnt2:
        answer.append(2)
    if m == cnt3:
        answer.append(3)
        
    return answer
  
  
  #  success

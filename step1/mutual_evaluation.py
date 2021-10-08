###first code###

def solution(scores):
    answer = ''
    student_score = list(map(list,zip(*scores)))
    print(student_score)
    
    for num, score in enumerate(student_score) :
        if score[num] == max(score) or score[num] == min(score) :
            del score[num]
        average = sum(score)/len(score)    
        if average <50 :
            answer += 'F'
        elif 50 <= average <70 :
            answer += 'D'
        elif 70 <= average <80 :
            answer += 'C'
        elif 80 <= average <90 :
            answer += 'B'
        else :
            answer += 'A'
           
    return answer
  
  ### test error
  # because if the condition is the same value as oneself, it is not excluded
  
  
  ## second code ##
  def solution(scores):
    answer = ''
    student_score = list(map(list,zip(*scores)))
    print(student_score)
    
    for num, score in enumerate(student_score) :
        if score.count(score[num]) == 1 and \   # 조건 하나 추가
           score[num] == max(score) or score[num] == min(score) :
            del score[num]
        average = sum(score)/len(score)    
        if average <50 :
            answer += 'F'
        elif 50 <= average <70 :
            answer += 'D'
        elif 70 <= average <80 :
            answer += 'C'
        elif 80 <= average <90 :
            answer += 'B'
        else :
            answer += 'A'
           
    return answer
  
  
  

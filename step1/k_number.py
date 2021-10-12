#Scenario
#[i-1:j]slicing 
#exception  i>j , j-(i+1)<k
# [k-1] return 
# answer append

def solution(array, commands):
    
    answer = []
    for i, j, k in commands :
        cut = array[i-1:j]
        if i != j:
            cut.sort()
        answer.append(cut[k-1])
    return answer

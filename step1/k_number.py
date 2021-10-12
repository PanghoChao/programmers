#Scenario
#[i-1:j]slicing 
#exception  i>j , j-(i+1)<k
# [k-1] return 
# answer append

def solution(array, commands):
    
    answer = []
    for i, j, k in commands :
        cut = array[i-1:j]
        if i > j :
            continue
            #indexerror
        if i != j:
            cut.sort()
        if j-i-1 < k :
            continue
            #indexerror
        answer.append(cut[k-1])
    return answer

# except 는 편의상 continue 로 대체

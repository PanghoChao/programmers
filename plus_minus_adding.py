def solution(absolutes, signs):
    
    for i in range(len(signs)):
        if signs[i] == True:   #sign배열안에 있는게 문자열이아니라 boolean임을 알게 되었다면, sign[i]만 써도 된다.
            continue
        else:
            absolutes[i] *= (-1)
    answer = sum(absolutes)
    print(answer)
    return answer

  

# 문제이해 
url = 'https://blog.naver.com/sobrightlf/222554571209'

# code
def solution(brown, yellow):
 
    divis = []
    grsr = yellow + brown
    for i in range(1, int(grsr**(1/2)) +1): #약수 범위
        if grsr % i == 0 : 
            a = grsr// i
            divis.append([a,i]) 
            
            
    for garo, sero in divis :
        if (brown == (garo+ sero -2) *2) and (yellow == (garo - 2)* (sero - 2)): #답이면
            answer= [garo,sero]
    return answer
  
  
  #success 
  #score(+1)

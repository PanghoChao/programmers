## frist code
## defaultdict 아니면 Counter로 쉽게 풀수가 있다.
from collections import defaultdict
def solution(clothes):
    answer = 1
    camouflage= defaultdict(list)

    for i, j in clothes :
        camouflage[j].append(i)


    for l in camouflage.values() :
        print(l)
        answer *=(len(l)+1) 

    answer-=1

    return answer
  
   #success

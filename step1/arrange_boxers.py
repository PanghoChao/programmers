#복서_정렬하기 


from collections import defaultdict
def solution(weights, head2head):
    answer = []
    rank_dict = defaultdict(list) 
    
    for num, w_or_l in enumerate(head2head) : 
        #전체 싸운 횟수
        entir = len(w_or_l) - w_or_l.count('N')
        if entir != 0:
            rank_dict[num].append((w_or_l.count('W')*100)// entir)
        if entir == 0 :  
            rank_dict[num].append(0)
        cnt = 0  #자기보다 무거운 선수 이긴 횟수 카운트하기
        for num2, result in enumerate(w_or_l):
            
            if result == 'W':
                if weights[num] < weights[num2]: #몸무게가 큰 경우만
                    cnt += 1
        rank_dict[num].append(cnt) 
        rank_dict[num].append(weights[num]) # 자기 몸무게 
        #rank_dict[num].append(num+1) #안해도 될 것 같음
        
    KeyList = sorted(rank_dict.items(), key=lambda s : (s[1][0], s[1][1],s[1][2]) ,reverse =True)

    for i in KeyList:
        answer.append(i[0]+1)

    return answer
  
  
  #but test error

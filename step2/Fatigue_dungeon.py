# 참고링크는 추후에
#
# code

def solution(k, dungeons):
    stack = [[k,[]]]
    cnt= 0    
    l = len(dungeons)
    while stack:
        energy,gone= stack.pop()
        for i in range(l):
            a, b = dungeons[i]
            
            if i not in gone and energy >= a: #가지않았고, 피로도제한도 통과되면
            
                stack.append([energy- b,gone+[i]]) #에너지계산과 방문기록
            else: 
                cnt = max(len(gone), cnt)
            
            
    return cnt

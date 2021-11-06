# 문제이해
https://blog.naver.com/sobrightlf/222559328868
  
#code

def solution(str1, str2):
    set1, set2 = [], []
    for idx1 in range(len(str1)-1):
        if str1[idx1].isalpha() and str1[idx1+1].isalpha():
            set1.append((str1[idx1]+str1[idx1+1]).lower())
        

    for idx2 in range(len(str2)-1):
        if str2[idx2].isalpha() and str2[idx2+1].isalpha():
            set2.append((str2[idx2]+str2[idx2+1]).lower())

    a,b = len(set1), len(set2)
    if a ==0 and b ==0 :
        return 65536
    
    cnt = 0
    for i in set1 : 
        if i in set2 :
            cnt += 1
            set2.remove(i)        
        
    print(cnt)
    answer = 65536 * cnt//(a+b-cnt)
    return answer

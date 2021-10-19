#문제이해 
# ????????????????????????????????????
# I don't understand..

# 먼저 LRU에대해 알아야한다. 
# https://blog.naver.com/sobrightlf/222541629726


#예상시나리오 

'''
구조를 알았으니 파이썬으로 구현하는법은 어렵지않다. 


if num in cache : # 캐시안에 해당 데이터가 있으면
    cache.pop(cache.index(num)) #빼주고
    cache.append(num) #다시 넣는다. 

else: # 데이터가 없는 경우라면
   cache.pop(0) #가장 오래된 데이터를 빼주고
   cache.append(num) #새로운 값을 넣는다.
   
   
'''
#first code
def solution(cacheSize, cities):
    answer = 0
    cache = []
   
    
    for data in cities:
        if cacheSize == 0 :
            answer += 5
            continue
        
        if data not in cache : #안에 없으면
            answer += 5 #cache miss
            if len(cache) >= cacheSize: #cache size
                cache.pop(0)
            cache.append(data)
        else : #안에 있다면
            answer += 1 #cache hit
            cache.pop(cache.index(data))
            cache.append(data)
    
    
    return answer
  
  
# Error 
# need lower(). 대소문자구분을 없애야한다.
data = data.lower()  
# for문 밑에 추가해주면 통과한다.

# success

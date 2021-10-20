
# 프로그래머스 문제중에 캐시에서 
# LRU 알고리즘을 구현하는 문제가 나왔었다. 
# 물론 최근걸앞으로 땡기고, 오래된걸 뒤로 미뤄 만드는 알고리즘이라 그리 어렵지는 않았다.
# 그래서 이번엔 LFU알고리즘을 구해 하고자 한다.


#first code
# 예상 답 {{2: 3, 
#          3: 3, 
#          5: 1,
#          1: 1}}
nums= [1,2,3,4,2,2,3,3,5,1]

cache_size = 4
for num in nums:
    if num in cache_dict:  # 데이터가 cache_dict안에 있다면    

        cache_dict[num]  += 1  # 카운트하나 올려준다.

    else :                            # 데이터가 cache_dict 안에 없는 값이면          

        if  len(cache_dict) < cache_size :  # 공간이 있다면 

            cache_dict[num] = 1

        else :                                             # 공간이 없다면

            cache_list = sorted(cache_dict.items(), key = lambda x : x[1], reverse = True)

        # value값(conut횟수)에 맞춰 정렬해준다. 근데 반환값이 list 이기에 마지막 값을 빼고
            cache_list.pop()
            cache_dict.clear()
            for key, value in cache_list :  #다시 딕셔너리로 바꿔준다.
                cache_dict[key] = value
            cache_dict[num] = 1

print(cache_dict)
#{1: 2, 2: 3, 3: 3, 4: 1}


# Error 
# count가 1인 값들의 우선순위가 매겨지지 않는다. 우선순위가 매겨지지 않는다.
# 그냥 들어온데로 앞에 위치하니, 스택구조가 아닌 큐로 구현해보자


# second code

nums= [1,2,3,4,2,2,3,3,5,1]

cache_dict = {}

cache_size = 4
for num in nums:
    if num in cache_dict:  # 데이터가 cache_dict안에 있다면    

        cache_dict[num]  += 1  # 카운트하나 올려준다.

    else :                            # 데이터가 cache_dict 안에 없는 값이면          

        if  len(cache_dict) < cache_size :  # 공간이 있다면 

            cache_dict[num] = 1

        else :                                             # 공간이 없다면

            cache_list = sorted(cache_dict.items(), key = lambda x : x[1])
            # value값(conut횟수)에 맞춰 정렬해준다. 근데 반환값이 list 이기에 마지막 값을 빼고
            cache_list.pop(0)
            cache_dict.clear()
            for key, value in cache_list :  #다시 딕셔너리로 바꿔준다.
                cache_dict[key] = value
            cache_dict[num] = 1

print(cache_dict) 

# {5: 1, 2: 3, 3: 3, 1: 1}

# 순서는 다르지만 성공했다. 
# 혹시 들어가는 값이 숫자 작은값 부터인가 해서 다른 값도 실험해보자 

nums= [4,3,2,1,2,2,3,3,5,4]
#{2: 3, 3: 3,5 : 1,  4: 1}
cache_dict = {}

cache_size = 4
for num in nums:
    if num in cache_dict:  # 데이터가 cache_dict안에 있다면    

        cache_dict[num]  += 1  # 카운트하나 올려준다.

    else :                            # 데이터가 cache_dict 안에 없는 값이면          

        if  len(cache_dict) < cache_size :  # 공간이 있다면 

            cache_dict[num] = 1

        else :                                             # 공간이 없다면

            cache_list = sorted(cache_dict.items(), key = lambda x : x[1])
            # value값(conut횟수)에 맞춰 정렬해준다. 근데 반환값이 list 이기에 마지막 값을 빼고
            cache_list.pop(0)
            cache_dict.clear()
            for key, value in cache_list :  #다시 딕셔너리로 바꿔준다.
                cache_dict[key] = value
            cache_dict[num] = 1
            
print(cache_dict)
#{5: 1, 3: 3, 2: 3, 4: 1}


# success 했다. 
# 이로써 간단한 LFU알고리즘은 딕션너리와 큐로 구현 가능하다.

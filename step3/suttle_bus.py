# 예상시나리오

'''
계산하기 쉽게 모두 분으로 전환해준다. 

초기값 : [9 , 0]  =>  [시간 , 분] 
9 *60 =  540 분으로 전환
total_m = m #셔틀 탈수있는 모든 인원
crew_set = []
shuttle_t = []
if n == 1 : #9시 셔틀을 타야댐

else : 
    for  i in rang(n)     
        add_t= t x (i)    #막차 셔틀 시간
        막차 시간  = 초기값 + add_t
        shuttle_t.append(막차시간) 
    total_m = n x m  #  셔틀 탈 수 있는 모든 인원
    
crew  =  0

for i in timetable :
    arrival = i.split(":")   => ['HH', 'MM']
    arrival_m = int(arrival[0])*60 + int(arrival[1])   # 분으로 정렬
    
    if 막차 시간 > arrival_m:     #막차 시간 보다 일찍 온 경우 
        crew_set.append(arrival_m)          # 여기서 셔틀 타는 크루 집단을 다시 모아준다.

   else: 
         딱히 영향 없음

if len(crew_set) >= total_m :  #콘이 못타게 되는 경우 
       crew_set.sort(revers=True) # 내림차순으로 정렬 해주고 
       
       for  t in shuttle_t: # 각 시간별
              while total_m > 1 :  #total_m =1 이 되면
                   crew_t = crew_set.pop()   

                   if  t  >= crew_t : # 시간 전에 왔다면 전체에서 빠지는게 맞음
                       total_m -= 1       

                   else : 
                       break

              answer = crew_set.pop() -1  # 막차 타기위해 여기 인덱스 시간보다 1분 일찍간다. 

else :  # 콘이 무조건 탈수 있는 경우 
     answer = 막차 시간



Tip . 첫차보단 늦게 왔지만, 막차보다 빨리온경우 -> 첫차의 인원이 꽉차지않아도 첫차는 못탐
      막차 전 셔틀을 기다렸지만, 꽉차서 막차까지 기다리게 되는 경우 = > 이경우  막차전 셔틀을 
      기다린 시간보다 빨리 와야 할 수도 있다.
        '''

# 예상시나리오 랑 예상 코드를 기반으로 
# first code
def solution(n, t, m, timetable):
    start_t = 540
    total_m = m
    crew_set = []
    shuttle_t = []
    last_t= 0
    answer = ''


    if n != 1:  #
        for i in range(n):
            add_t = t*i
            last_t = start_t + add_t
            shuttle_t.append(last_t)
        
        total_m = n * m
    

    for time in timetable:
        arrival = time.split(":")
        arrival_m = int(arrival[0])* 60 + int(arrival[1]) # 분으로 정렬
        if last_t > arrival_m :
            crew_set.append(arrival_m)
    

    if len(crew_set) >= total_m: #콘이 못타게 되는경우 
        crew_set.sort(reverse=True) # 내림차순으로 정렬
        for t in shuttle_t: #각 시간별
            while total_m > 1: # 콘이 탈수있는 한자리 남게 무한루프
                crew_t = crew_set.pop()
                if t >= crew_t:
                    total_m -= 1
                else:
                    break
            answer= crew_set.pop() - 1 
            break
    else : # 막차 시간에맞추면 무조건 탑승
        answer = last_t
    return answer

  
  ## Interim check
print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
print(solution(2,10,2,["09:10", "09:09", "08:00"]))
print(solution(2,1,2,["09:00", "09:00", "09:00", "09:00"]))
print(solution(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1,1,1,["23:59"]))
print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))

 
  # Error

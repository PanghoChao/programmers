#문제이해 
https://blog.naver.com/sobrightlf/222560174142
    
    
#code 1
def solution(arr):

    cnt1 = arr.count(1)
    cnt2 = arr.count(2)
    cnt3 = arr.count(3)

    mx_cnt = max(max(cnt1, cnt2),cnt3)
    print(mx_cnt)
    answer = [mx_cnt - cnt1,mx_cnt - cnt2,mx_cnt - cnt3]
    
    return answer
  
  
#code 2
def solution(log):

 
    study = []
    study_time = 0
    for t in log:  #시간 하나 
        h,m = t.split(":")  #시와 분 나누기 
        t_m = (int(h)* 60) + int(m)
        
        if not study : #study가 비어있으면
            study.append(t_m)    
        else:
            start_t = study.pop()
            real_t = t_m - start_t    
            if t_m - start_t < 5: #무효화
                continue
            if 5 <= real_t <= 105: #5보다 크고 1시간 45분보다 작은
                study_time += real_t
            else:
                study_time += 105
    
    h = str(study_time // 60)
    m = str(study_time % 60)
    
    if len(h) < 2 :
        h = '0'+str(h)
    if len(m) < 2 :
        m = '0'+str(m)
    
    answer = h + ":" + m  
            
    return answer
  
  
  #code 3 
  def solution(ings, menu, sell):
    answer = 0
    material_dict = {}
    f_profit_dict = {}
    for material in ings: #재료 가격표 만들기
        m, m_price= material.split(" ")
        material_dict[m] = int(m_price)
            
    for food in menu : # 음식 수익표 만들기 
        f, f_material , f_price = food.split(" ")
        
        real_price = 0
        for f_m in f_material:
             real_price += material_dict[f_m] #모든 재료값 더하기
        profit = int(f_price) - real_price #수익
        
        f_profit_dict[f] = profit

    # print(material_dict, f_profit_dict)    


    for sell_cnt in sell :
        f, f_cnt = sell_cnt.split(" ")
        answer += f_profit_dict[f] * int(f_cnt) 
        
    return answer

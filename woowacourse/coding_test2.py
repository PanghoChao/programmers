#문제이해 
https://blog.naver.com/sobrightlf/222560276973


# code 4

from collections import deque
def solution(s):
    #1.맨앞과 맨뒤를 비교해서 같으면 맨앞의 문자를 뒤로 보내준다. 
    #2. 그리고 문자의 갯수를 작은수부터 차례대로 입력한다.
    answer = []
    s = deque(s)
    while True: #1번 수행
        alpha = s.popleft()
        if alpha == s[-1]:
            s.append(alpha)
        else: 
            s.appendleft(alpha)
            break
            
    stack = [] # 2번 수행
    cnt =0    
    for i in s:
        if i not in  stack:  
            if cnt > 0 :
                answer.append(cnt)
            cnt = 0
            stack.clear()
            stack.append(i) 
        if i in stack:
            cnt += 1
    answer.append(cnt)
    answer.sort()
        
    return answer
'''
print(solution(("w"*998) +"ow")) #1번이 최대회ㅅ수가 되지만, 
#2번에서연산 속도가 줄어듬
'''

# code 5

def solution(rows, columns):
    # 행열이 서로 나누어 떨어지는 경우가 아니라면 0칸을 다 채울수 있다.
    # 행열 값이 0 인경우 카운트하면 된다.
    metrix = [[0 for _ in range(columns)] for _ in range(rows)]
    i,j = 0,0
    metrix[0][0] = 1
    if max(rows, columns) % min(rows, columns): #0을 없앨수 있는 경우    
        cnt = rows*columns -1
        while cnt :
            cnt -= 1
            before = metrix[i][j]

            if before % 2 == 1: #홀수이면
                if j + 1 == columns:
                    j = -1
                j += 1
                if metrix[i][j] != 0:   #겹치는 부위면
                    cnt +=1
                metrix[i][j] = before + 1                

            else: #짝수이면
                if i + 1 == rows:
                    i = -1
                i += 1
                if metrix[i][j] != 0: #겹치는 부위면
                    cnt +=1
                metrix[i][j] = before + 1   
 


    
    # 같은 위치를 반복해서 도는 경우 
    else: 
        while True:
            before = metrix[i][j]

            if before % 2 == 1: #홀수이면
                if j + 1 == columns:
                    j = -1
                j += 1
                metrix[i][j] = before + 1                

            else: #짝수이면
                if i + 1 == rows:
                    i = -1
                i += 1
                if i == 0 and j == 0 :
                    break            
                metrix[i][j] = before + 1   
           

    return metrix
  
 
# code 6
def solution(time, plans):
    # 휴가시간은 사용하면 점차 사라지기때문에 주의할 필요가 있다 .
    # 금요일은 퇴근시간 , 월요일은 출근시간에 맞춰 휴가를 쓰게 된다. 
    # 휴가 갈수 없을 경우 "호치민"을 반환해준다.
    answer = '호치민'
    fri = 18
    mon = 13 
    # PM 과 AM 통일 
    for country, start, end in plans:
        s_t = int(start[:-2])
        e_t = int(end[:-2])
        if 'PM' in start:               #24시로 바꿔준다.
            s_t = 12 + int(start[:-2])
        if 'PM' in end:
            e_t = 12 + int(end[:-2])
        
        # 휴가 시간 계산
        if fri > s_t  :
            if s_t <= 9.5:
                time -= 8.5
            else:
                time -= fri - s_t    
        if mon < e_t :
            if e_t >= 18:
                time -= 5
            else:
                time -= e_t - mon
        
        # 휴가 시간이 부족하면
        if time < 0 :
            return answer
        #휴가 갈 수 있으면 나라 바꿔준다.
        answer = country
        
    return answer

# print(solution(3,[["엘에이", "3PM", "2PM"]] )) #호치민 체크
# print(solution(9.5,[["엘에이", "9AM", "2PM"]] )) #금요일 출근 보다 먼저 출발하는 경우
# print(solution(8,[["엘에이", "3PM", "7PM"]] )) #월요일 퇴근 보다 늦게 도착하는 경우


# code  7
# 수정필요함 
def solution(grid, clockwise):
    # 삼각형이니까 연결고리가 3개씩은 있는거다.
    #1개 2개, 1개 2개 2개 , 1개 2개 2개 2개 
    answer = []
    floor = len(grid)
    f_num = len(grid)*2 +1 
    print(floor, f_num)
    if clockwise: #시계방향일 경우
        answer.append(grid[floor][0])
        pass
        
    else : #반시계 일경우 
        
        for i in range(floor) : 0 ~ 2
            if i == 0 :
                anwer.appen(grid[floor][f_num])
                continue
            floor_el = ""
            f = floor
            f_n = f_num
            element = i*2 + 1
            while element : 
                floor_el = "".join(grid[f-i][f_n - i])    
                element -= 1
        pass
        
        
    
    return answer

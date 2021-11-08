#우테코 1차 7번 문제

# code
def solution(grid, clockwise):

    answer = []
    floor = len(grid) - 1

    if clockwise: #시계방향일 경우
        answer.append(grid[floor][0]) #꼭대기 입력
        for i in range(1, floor+1): # 층수만큼 반복
            string = ""
            j = 2 * i
            k = 0
            while j:
                string += grid[floor-k][j]
                string += grid[floor-k][j-1]
                k += 1
                j -= 2
        
            string += grid[floor-i][0]  #마지막 추가
           
            answer.append(string)

    else : #반시계 일경우 
        answer.append(grid[floor][floor*2]) #꼭대기 입력
        for i in range(1, floor+1): #층수만큼 반복
            string = ""
            string += grid[floor - i][2*(floor - i)]
            j = 1
            k = 1
            while i*2 > j:
                string += grid[floor-i+k][2*(floor-i+1) - 1]
                string += grid[floor-i+k][2*(floor-i+1) - 2]
                k += 1
                j += 2
            answer.append(string)            

 
    
    return answer

print(solution(["1","234","56789"], False)) //['9', '487', '13265']
print(solution(["1","234","56789"], True)) //['5', '762', '98431']
print(solution(["A","MAN","DRINK","WATER11"], False)) //['1', 'K1R', 'NNIET', 'AAMRDAW']

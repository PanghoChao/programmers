#삽질한 내용은 블로그에서 
#깃허브에서는 이제부터 주요 내용만 정리 하고자한다.
https://blog.naver.com/sobrightlf/222546666309
  
#행렬 최단거리 문제는 왠만해선 BFS로 풀이하며
#이동거리를 담을 수 있는 복제의 행렬이 있는게 좋다.

# code
from collections import deque


def solution(maps):
    r = len(maps) # y축
    c = len(maps[0]) # x축
    
    virtual_map = [[-1 for _ in range(c) ]for _ in range(r)] #행렬 복제
    virtual_map[0][0] = 1 # 처음 이동거리 입력
    queue = deque()
    queue.append([0, 0]) # 처음 위치 입력
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        y, x  = queue.popleft()        

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <c and 0<=ny <r and maps[ny][nx] == 1 :
                if virtual_map[ny][nx] == -1:
                    virtual_map[ny][nx] = virtual_map[y][x] + 1  #기존 이동거리를 더해주면서 나간다.
                    queue.append([ny,nx])

    answer = virtual_map[-1][-1]
    return answer

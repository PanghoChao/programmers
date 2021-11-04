#문제이해
https://programmers.co.kr/learn/courses/30/lessons/12905
  
# code

def solution(board):
    answer = 0
    for i in range(0, len(board)):
        
        for j in range(0, len(board[0])):    
            if board[i][j] > 0 and i>0 and j>0:
                if  board[i-1][j] > 0 and\
                    board[i][j-1] > 0 and \
                    board[i-1][j-1] > 0 :
                    board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1]) + 1
        answer = max(max(board[i]),answer)                
      
    return answer**2

# 문제이해
# https://blog.naver.com/sobrightlf/222544980044


#예상 코드

def hanoi(n,a,b,c):

#갯수가 1개면 그냥 첫번째에서 두번째로 옮기면 된다.

   if n= 1:

      [a,c]

      return 1

# n-1개를 a에서 b 번으로 옮긴다 .

   [a,b] => hanoi(n-1, a,c,b)

​

# n번째 원판을 a에서 c 번으로 옮긴다. 

   [a,c]

​

# n-1개를 b에서 c로 옮긴다. 

   [b,c] => hanoi(n-1, b,a,c)

​

def solution(n):

   answer = [[]]

   a = 1

   b = 2 

   c = 3

   return answer
  
  
  
  #first code
  
  def hanoi(n,a,b,c,answer):

    #이동순서 
    if n == 1 :
        answer.append([a,c])
        return 0

    hanoi(n-1, a,c,b, answer)
    

    answer.append([a,c])

    hanoi(n-1, b,a,c, answer)
	
    return 0


def solution(n):
    answer= []
    a = 1
    b = 2
    c = 3
    hanoi(n,a,b,c, answer)
    return answer

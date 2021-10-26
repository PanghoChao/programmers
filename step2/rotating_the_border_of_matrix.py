
https://blog.naver.com/sobrightlf/222548886184

#code

#from collections import deque
def solution(rows, columns, queries):
    metrix = [[(i+1)+(columns*j) for i in range(columns)] for j in range(rows)] #행렬생성
    answer = []

    for x1,y1,x2,y2 in queries:
        queue= [0]
        mn = [ rows*columns ]  
        for my in range(y1-1, y2): #y값 이동
                q = queue.pop()
                n = mn.pop()
                num = metrix[x1-1][my]
                metrix[x1-1][my] = q
                queue.append(num)
                mn.append(min(n,num))

        for mx in range( x1, x2): # X값 이동
                q = queue.pop()
                n = mn.pop()
                num = metrix[mx][y2-1]
                metrix[mx][y2-1] = q
                queue.append(num)
                mn.append(min(n,num))


        for my in range(y2-2, y1-2, -1): # y값 -이동
                q = queue.pop()
                n = mn.pop()
                num = metrix[x2-1][my]
                metrix[x2-1][my] = q
                queue.append(num)
                mn.append(min(n,num))


        for mx in range(x2-2, x1-1,-1): #-x축 이동
                q = queue.pop()
                n = mn.pop()
                num = metrix[mx][y1-1]
                metrix[mx][y1-1] = q
                queue.append(num)
                mn.append(min(n,num))



        answer.append(mn.pop())
        metrix[x1-1][y1-1] = queue.pop()

    return answer


print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(100,97,[[1,1,100,97]]))

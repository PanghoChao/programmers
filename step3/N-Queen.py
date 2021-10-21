# 문제이해 및 분석
# https://blog.naver.com/sobrightlf/222543933427

# 예상 시나리오
'''
1. 일단 n= 1일때는 1이고, n<4 을때는 값이 0이다. 
2. n>= 4 때는 Q의 위치를 계산하는 알고리즘을 만들고
3. Q의 위치를 계산하는 알고리즘이 n번 돌았을때 이상이 없으면
4. count 갯수를 1 늘린다.


Q의 위치 계산하는 예상 코드 
N x N 행렬에 N개의 'Q'가  하나씩 들어 가야한다. 
Q의 최대 떨어질 수 있는 칸 수는 (N-1)개 이며
재귀함수를 사용한다. 
'''

#예상 수도코드
def Q_location(i, j , n, check, cnt):
   if  i <= n and  i not in check : # i가 n보다 작고, 빈자리면  
         check.append(i)  
         j  -= 1

   if len(check) == n :
         cnt += 1
         return cnt
      
   if j == 0 or i > n 
         return cnt

   for  k in range(2,n-1): 
       if i > k :
         cnt += Q_location(i-k, n , check,cnt)

       if i <= k: 
         cnt += Q_location(i+k, n , check,cnt)

    return cnt

def solution(n):
  cnt_set=[]
  for i  in range(1,n+1):
    j = n
    check = []
    cnt = 0
    cnt_set.append( Q_location(i, j , n, check, cnt))

#각 경우의수 다나옴
return sum(cnt_set)


###########################
###      first code     ###
###########################
def Q_location(i, j , n, check, cnt):
    check1= list(check)
    if 0< i <= n :
        if i not in check1 : # i가 빈자리면
            check1.append(i)
            j -= 1
            if j == 0 :
                if len(check1) == n:
                    cnt += 1
                return cnt 

            for k in range(2,n):
                if 0< i-k <= n :
                    cnt = Q_location(i-k,j, n , check1,cnt)

                if 0< i+k <= n:
                    cnt = Q_location(i+k,j, n , check1,cnt)
            return cnt 
        else : #빈자리가 아니면 굳이 할 필요가 없다.
            j = 0
            return cnt
    else:
        j = 0
        return cnt


def solution(n):
    cnt_set=[]
    for i in range(1, n+1):
        j = n
        check = []
        cnt = 0
        cnt_set.append( Q_location(i, j , n, check, cnt))

    #각 경우의수 다나옴
    return sum(cnt_set)
##
# Of course, error.
##

# Find Problem
# 대각선일 경우 제외 필요!

l = len(check)
for idx, m in enumerate(check):   #같은 대각선 제거
    if i == m + l - idx or i == m -(l - idx):
        return cnt

# so, add code

# Infinite code
def Q_location(i, j , n, check, cnt):
    check1= list(check)
    # if 0< i <= n :
    if i not in check1 : # i가 빈자리면
        check1.append(i)
        j -= 1
        l = len(check)
        for idx, m in enumerate(check):
            if i == m + l - idx or i == m -(l - idx):
                return cnt
        if j == 0 :
            if len(check1) == n:
                cnt += 1
            return cnt 

        for k in range(2,n):
            if 0< i-k <= n :
                cnt = Q_location(i-k,j, n , check1,cnt)

            if 0< i+k <= n:
                cnt = Q_location(i+k,j, n , check1,cnt)
        return cnt 
    else : #빈자리가 아니면 굳이 할 필요가 없다.
        j = 0
        return cnt



def solution(n):
    cnt_set=[]
    for i in range(1, n+1):
        j = n
        check = []
        cnt = 0
        cnt_set.append( Q_location(i, j , n, check, cnt))

    #각 경우의수 다나옴
    return sum(cnt_set)
  
  
  # 

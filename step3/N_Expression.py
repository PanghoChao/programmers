# 문제이해
https://blog.naver.com/sobrightlf/222557187442

# dynamic programming
# code
def solution(N, number):
    if N == number:
        return 1 

    #[set X 8]
    cnt = [set() for x in range(8)]
    # 각 set마다 기본수 'N' * i 수 초기화
    for i,x in enumerate(cnt, start=1):
        x.add(int(str(N)*i))
    
    # n일반화

    for i in range(1,8):  # i=4
        for j in range(i):  # j = 1 (0~3)
            for dp1 in cnt[j]:  #dp1 = NN
                for dp2 in cnt[i-j-1]: #dp2 =NNN
                        cnt[i].add(dp1+dp2)
                        cnt[i].add(dp1-dp2)
                        cnt[i].add(dp1*dp2)
                        if dp2 != 0 :
                            cnt[i].add(dp1//dp2)
        if number in cnt[i]:
            answer = i + 1
            break
    else:
        answer= -1

    return answer




print(solution(5,12))

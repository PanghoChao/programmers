##### first code ####

def solution(price, money, count):
    answer = 0
    for i in range(1, count +1 ):
        answer += (price * i)
    

    return (answer - money)





#### repair code ####

def solution(price, money, count):
    all_price = 0
    for i in range(1, count +1 ):
        all_price += (price * i)
    
    if all_price < money:
        answer = 0
    else :
        answer = all_price -money

    return answer
    
    

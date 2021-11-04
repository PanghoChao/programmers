#문제이해
https://blog.naver.com/sobrightlf/222557633893
  
  # 
  
  def solution(numbers):
    result=[]
    for num in numbers:
        if num == 1 : 
            result.append(num+1)
            continue
            
        if num % 2 == 0 :
            result.append(num+1)
            continue
            
        if num == 3 :
            result.append(num+2)
            continue
            
        for i in range(2, num):
            if (num % 2**(i)) == (2**(i-1) - 1):
                result.append(num + 2**(i-2))
                break

    return result

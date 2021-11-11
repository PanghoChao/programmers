#first code

import pprint 

def solution(nums):
    answer = 0
    
    mx = len(nums)/2
    d_phonekemon = len(set(nums))
 
    
    if mx <= d_phonekemon:
        answer = mx
    else : 
        answer = d_phonekemon
    
    return answer
  
#repeated number => set_function 
#success

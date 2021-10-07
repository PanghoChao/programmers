##규칙을 찾아 별도 배열을 만들어 계산##


def solution(word):
    words = ["A","E","I","O","U"]
    squence_num = [781, 156, 31, 6, 1]
    answer = 0
    for word_idx, alph in enumerate(word):
        answer = answer + words.index(alph) * squence_num[word_idx] + 1
        
    return answer
  
  
  # 재귀적 표현으로 계산

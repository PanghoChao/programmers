#list 와 dict를 활용하면 비교적 쉬운문제


def solution(record):
    uid_dict ={}
    act_list = []
    answer = []
    for infor in record:
        p_infor = infor.split()
        if p_infor[0] != 'Leave':
            uid_dict[p_infor[1]] = p_infor[2]
        act_list.append(p_infor[:2])
    
    for out_put , uid in act_list:
        if out_put == 'Enter' :
            answer.append(uid_dict[uid]+"님이 들어왔습니다.")
        if out_put == 'Leave' :
            answer.append(uid_dict[uid]+"님이 나갔습니다.")
        else: #change일때
            continue

    
    return answer

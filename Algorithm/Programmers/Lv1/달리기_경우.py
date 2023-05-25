# https://school.programmers.co.kr/learn/courses/30/lessons/178871


def solution(players, callings):
    l = 0
    name = ''
    dic1 = {}
    dic2 = dict()
    
    for i in range(len(players)):
        dic1[i] = players[i]
        dic2[players[i]] = i
        
    
    for i in callings :
        l = dic2[i] # i 위치가져오기
        name = dic1[l-1]
        dic1[l-1], dic1[l] = dic1[l],dic1[l-1]
        dic2[i],dic2[name] = dic2[name], dic2[i]
        

    answer = list(dic1.values())
    return answer
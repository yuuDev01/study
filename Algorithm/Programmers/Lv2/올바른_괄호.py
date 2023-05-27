#출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):   
    data = []
    
    for i in s :
        if i == ')' and data:
            data.pop()
        else : data.append(i)
        
    return True if not data else False
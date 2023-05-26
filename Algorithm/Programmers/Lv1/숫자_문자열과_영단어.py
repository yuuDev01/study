# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/courses/30/lessons/81301

numD = {'zero':'0','one':'1','two':'2','three':'3', 'four':'4','five':'5','six':'6', 'seven':'7', 'eight':'8','nine':'9'}

def solution(s):
    answer = ''
    n =''
    for i in s :
        if i.isdigit() :
            answer +=i
        else :
            n+=i
            if n in numD.keys():
                answer += numD[n]
                n = ''
    return int(answer)


# replace 사용 - 시간 복잡도 고려X
# def solution(s):
#     answer = 0
#     for k, v in numD.items():
#         s= s.replace(k,v)
#     return int(s)
# https://school.programmers.co.kr/learn/courses/30/lessons/81301

numD = {'zero':'0','one':'1','two':'2','three':'3', 'four':'4','five':'5','six':'6', 'seven':'7', 'eight':'8','nine':'9'}

def solution(s):
    answer = 0
    for k, v in numD.items():
        s= s.replace(k,v)
    return int(s)
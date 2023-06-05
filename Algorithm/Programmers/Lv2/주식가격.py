# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque 
def solution(prices):
    prices = deque(prices)
    n = 0
    answer = [0]*len(prices)
    while prices:
        price = prices.popleft()
        if not prices : break
        for i in prices:
            if i >= price :
                answer[n] += 1
            else : 
                answer[n]+=1
                break
        n+=1 
    return answer

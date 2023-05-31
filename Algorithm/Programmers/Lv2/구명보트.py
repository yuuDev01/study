# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque
def solution(people, limit):
    answer = 0
    #내림차순으로 정렬
    people.sort(reverse = True)
    people = deque(people)
    #people가 있을때까지 반복
    while people :
        if len(people) <= 1: 
                answer += 1
                break
        v = people.popleft() #왼쪽 첫번째 뽑아내기
        if v > limit//2 : #무게제한의 절반보다 클 경우
            if v + people[-1] <= limit : 
                people.pop()
            answer += 1
        else : #무게제한 절반보다 작거나 같을 경우
            answer += (len(people)+1)//2 + (len(people)+1)%2
            break
    return answer
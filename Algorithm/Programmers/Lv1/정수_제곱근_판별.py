#출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    answer = 0
    if n == 1 : 
        return 4
    for i in range(1,n//3):
        if i ** 2 == n : 
            answer = i
            break
    if answer ==  0 : return -1
    return (answer+1)**2
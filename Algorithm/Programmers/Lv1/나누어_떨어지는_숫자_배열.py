#출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/courses/30/lessons/12910


def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    return [-1] if len(answer) == 0 else sorted(answer)
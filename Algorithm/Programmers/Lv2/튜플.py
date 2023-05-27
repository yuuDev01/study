# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    s = s[2:-2].split('},{')
    data = []

    for i in s:
        n = list(map(int, i.split(',')))
        data.append(sum(n))
    
    data.sort()

    return  [ data[i] if i == 0 else data[i]-data[i-1]  for i in range(len(data)) ]
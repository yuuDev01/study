#출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/courses/30/lessons/12914

```
def solution(n):
    if n == 1 or n == 2 :
        return n
    data = [1,2]
    for i in range(2,n):
        data.append(data[i-1]+data[i-2])
    
    return data[-1]%1234567
```
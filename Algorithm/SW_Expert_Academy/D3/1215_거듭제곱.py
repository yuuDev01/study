# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14dUIaAAUCFAYD
# 1217. 재귀함수를 이용한 거듭제곱 

def solution(n, m, i):
    if m < i:
        return 1
    else:
        return n * solution(n, m, i+1)


for _ in range(10):
    t = int(input())
    n, m = map(int, input().split())
    print('#'+str(t), solution(n, m, 1))
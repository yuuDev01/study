# 1948. 날짜 계산기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PnnU6AOsDFAUq

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())
for test_case in range(1, T + 1):
    n1, n2, m1, m2 = map(int, input().split())
    d1 = sum(day[:n1-1])+n2
    d2 = sum(day[:m1-1])+m2
    print(d2-d1+1)
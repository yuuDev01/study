# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh
# 행렬 행/열 위치 바꾸기
T = 10
for test_case in range(T):
    N = int(input()) # 테스트 케이스 번호
    matrix = []
    maxNum = 0
    x, y = 0, 0
    for i in range(100):
        n = list(map(int, input().split()))
        matrix.append(n)
        x += n[i]
        y += n[99 - i]
        if maxNum < sum(n):
            maxNum = sum(n)  # 각 행의 합 중 최대값 구하기
    if maxNum < x:
        maxNum = x
    elif maxNum < y:
        maxNum = y
    matrix2 = list(map(list, zip(*matrix)))  # 행렬 회전
    for i in range(100):
        if maxNum < sum(matrix2[i]):
            maxNum = sum(matrix2[i])  # 각 행의 값 중 최대값 구하기

    print('#' + str(test_case+1), maxNum)

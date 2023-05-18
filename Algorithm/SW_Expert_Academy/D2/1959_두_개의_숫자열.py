# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq
# 1959. 두 개의 숫자열


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    maxV = 0

    A = list(map(int, input().split())) # N
    B = list(map(int, input().split())) # M

    if N < M:
        N, M = M, N
        A, B = B, A
    for i in range(0, N-M+1):
        X = 0
        for j in range(0, M):
            X += A[i+j]*B[j]
        if maxV < X : maxV = X

    print('#'+str(test_case), maxV)
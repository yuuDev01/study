# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWE_ZXcqAAMDFAV2
# 3431. 준환이의 운동관리

T =int(input())

for test_case in range(1, T+1):
    L,U,X = map(int, input().split())
    n = 0
    if X < L :
        n = L - X
    elif L <= X <= U :
        n = 0
    else :
        n = -1

    print('#'+str(test_case), n )

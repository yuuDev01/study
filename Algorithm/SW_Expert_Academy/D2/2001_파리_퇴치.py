# 2001. 파리 퇴치
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N : 배열크기 NXN  M : 파리채크기 MxM
    mlist = []
    max = 0
    for i in range(N):
        mlist.append(list(map(int, input().split())))
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for k in range(M):
                for l in range(M):
                    s += mlist[i+k][j+l]
                    # print(s)
            if max < s : max = s
    print('#'+str(test_case),max)
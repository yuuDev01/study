# 1961. 숫자 배열 회전
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq


T = int(input())
for test_case in range(1, T+1):
    print('#'+str(test_case))
    N = int(input())
    nlist = []
    mlist = []
    slist = [['0']*3 for _ in range(N)]
    for _ in range(N):
        mlist.append(list(map(str, input().split())))
    for i in range(3):
        mlist = list(map(list, zip(*mlist[::-1])))
        for j in mlist:
            nlist.append(j)
    nlist = nlist[::-1]
    for i in range(3):
        for j in range(N):
            s = nlist.pop()
            slist[j][i] = ''.join(s)
    for i in range(N):
        print(' '.join(slist[i]), end=' ')
        print()

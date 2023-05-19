# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq
# 1954. 달팽이 숫자
# 다시 풀기


T = int(input())
for test_case in range(1, T+1):
    print('#'+str(test_case))
    N = int(input())
    mlist = [[0]*N for _ in range(N)]
    p1,p2 = 0,0
    d = 0
    chk = []
    for i in range(1,N*N+1):
        if mlist[p1][p2] == 0  :
            mlist[p1][p2] = i
        chk.append(i)
        # 방향 알기
        if d == 0 : #오
            p2 +=1
            if p2 == N or mlist[p1][p2] in chk :
                p2 -=1
                p1 +=1
                d = 1
        elif d == 1 : #아래
            p1 += 1
            if p1 == N or mlist[p1][p2] in chk :
                p1 -= 1
                p2 -= 1
                d = 2
        elif d == 2 : # 왼
            p2 -= 1
            if p2 < 0 or mlist[p1][p2] in chk :
                p2 +=1
                p1 -=1
                d = 3
        elif d == 3 : #위
            p1 -= 1
            if p1 < 0 or mlist[p1][p2] in chk:
                p1 +=1
                p2 +=1
                d = 0

    for i in mlist:
        for j in i:
            print(j, end=' ')
        print()
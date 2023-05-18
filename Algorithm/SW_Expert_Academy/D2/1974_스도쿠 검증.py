#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq
# 1975. 스도쿠 검증


T = int(input())
for test_case in range(1, T + 1):
    mlist = []
    answer = 0
    for _ in range(9):
        mlist.append(list(map(int, input().split())))
    mlist2 = list(map(list, zip(*mlist)))  # 회전

    for i in range(9):
        if sum(mlist2[i]) == 45 and sum(mlist[i]) == 45: # 가로 세로 둘다 합 45일 경우
            answer = 1
        else:
            answer = 0
            break
    # 3 x 3 작은 격자 확인
    if answer == 1:
        for i in range(0,9,3):
            n = sum(mlist[i][0:3]) + sum(mlist[i+1][0:3]) + sum(mlist[i+2][0:3])
            m = sum(mlist[i][3:6]) + sum(mlist[i+1][3:6]) +sum(mlist[i+2][3:6])
            k = sum(mlist[i][6:]) + sum(mlist[i+1][6:]) + sum(mlist[i+2][6:])
            if n and m and k == 45:
                answer = 1
            else :
                answer = 0
                break

    print('#' + str(test_case), answer)

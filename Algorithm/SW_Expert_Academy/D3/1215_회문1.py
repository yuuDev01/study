# 1215. [S/W 문제해결 기본] 3일차 - 회문1
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    cnt = 0
    mylist =[['A']*8 for _ in range(8)]
    for i in range(8):
        s = input()
        for j in range(8):
            mylist[i][j] = s[j]
    mylist2 = list(map(list, zip(*mylist)))
    for i in range(8):
        for j in range(0,9-N):
            x1 = ''.join(mylist[i][j:j+N])
            x2 = ''.join(mylist2[i][j:j+N])
            if x1 == x1[::-1] :
                cnt+=1
            if x2 == x2[::-1]:
                cnt+=1
    print(cnt)
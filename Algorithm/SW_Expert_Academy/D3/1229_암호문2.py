# 1229. [S/W 문제해결 기본] 8일차 - 암호문2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14yIsqAHYCFAYD

T = 10
for test_case in range(1, T + 1):
    N = int(input())  # 원본 암호문의 길이
    plist = list(map(str, input().split()))  # 원본 암호문
    c = int(input())  # 명령어 개수
    clist = list(map(str, input().split()))  # 명령어 I 삽입 D 삭제
    nlist = []
    ss = []
    for i in clist:
        if i != 'I' and i != 'D':
            ss.append(i)
        else:
            nlist.append(ss)
            ss = [i]
    nlist.append(ss)
    nlist = nlist[1:]
    for i in nlist:
        h = i[0]
        x = int(i[1])
        y = int(i[2])
        if h == 'I': #삽입
            z = i[3:]
            for j in range(y):
                plist.insert(x+j, z[j])
        elif h =='D' : #삭제
            for j in range(y):
                plist.pop(x)
    print('#' + str(test_case),end=' ')

    for i in range(10):
        print(str(plist[i]), end=' ')
    print()
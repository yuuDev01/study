# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14w-rKAHACFAYD

T = 10
for test_case in range(1, T+1):
    N = int(input()) # 원본 암호문의 길이
    plist = list(map(str, input().split())) # 원본 암호문
    c = int(input()) #명령어 개수
    clist = list(map(str, input().split('I'))) # 명령어
    clist = clist[1:]
    nlist =[]
    print('#' + str(test_case),end=' ')
    for i in clist:
        nlist.append(i.split())
    for i in nlist:
        x = i[0]
        y = i[1]
        z = i[2:]
        for j in range(int(y)):
            plist.insert(int(x)+j,z[j])
    for i in range(10):
        print(str(plist[i]), end=' ')
    print()
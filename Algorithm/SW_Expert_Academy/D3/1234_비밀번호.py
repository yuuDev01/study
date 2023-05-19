#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD

T = 10
for test_case in range(1, T+1):
    N, M = map(str, input().split()) # N : 문자열의 총 수  M : 문자열
    toggle = True
    while toggle:
        s = ''
        for i in range(len(M)-1):
            s = M[i]
            if s == M[i+1] :
                M = M.replace(M[i:i+2],'')
                break
            elif i == len(M)-2 :
                toggle = False

    print('#'+str(test_case),M)
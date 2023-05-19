# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq
# 1979. 어디에 단어가 들어갈 수 있을까

T = int(input())
for test_case in range(1,T+1):
    N, K = map(int, input().split())
    mlist = []
    cnt = 0
    for i in range(N):
        mlist.append(list(map(str, input().split())))
    nlist = list(map(list, zip(*mlist)))
    for i in nlist :
        mlist.append(i)
    for i in mlist:
        s = ''.join(i)
        for j in s.split('0') :
            if j == '1'*K :
                cnt+=1
    print('#'+str(test_case),cnt)
#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pl0Q6ANQDFAUq


nlist = [2,3,5,7,11]
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    print('#' + str(test_case), end=' ')
    cnt, x = 0, 0

    for i in range(len(nlist)):
        if N % nlist[i] == 0:
            x = nlist[i]
            while N % x == 0 :
                x *= nlist[i]
                cnt+=1
            N //= (nlist[i]**cnt)
        print(cnt, end=' ')
        cnt = 0
    print()

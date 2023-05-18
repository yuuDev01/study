# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq
# [D2] 2005.파스칼의 삼각형

T = int(input())
for test_case in range(1, T + 1):
    print('#' + str(test_case))
    N = int(input())  # 삼각형 크기
    mylist = []
    mylist.append([1])
    print(1)
    for i in range(1, N):
        n = []
        for j in range(i + 1):
            if j == 0 or j == i:
                n.append(1)
            else:
                n.append(mylist[i - 1][j - 1] + mylist[i - 1][j])
        mylist.append(n)
        i = list(map(str, n))
        s = ' '.join(i)
        print(s)

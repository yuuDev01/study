# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB
# 2085. 농작물 수확하기

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    mlist = []
    m = (n-1)//2
    sumn = 0
    cnt = 1
    for i in range(n):
        s = ''
        p = str(input())
        mlist.append(list(p))

        p1,p2 =0,0
        if i == 0 or i == n - 1:
            sumn += int(mlist[i][m])
        elif i > m:
            p1 = list(map(int, mlist[i][cnt:m]))
            p2 = list(map(int, mlist[i][m+1:m+1+len(p1)]))
            sumn += sum(p1+p2)+int(mlist[i][m])
            cnt += 1
        else:
            p1 = list(map(int, mlist[i][m - i:m]))
            p2 = list(map(int, mlist[i][m+1:m + i +1]))
            sumn += sum(p1+p2)+int(mlist[i][m])
    print('#' + str(test_case), sumn)
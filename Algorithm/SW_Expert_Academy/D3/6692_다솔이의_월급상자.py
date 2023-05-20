# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWdXofhKFkADFAWn

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    s = 0
    for i in range(n):
        x, y = map(float, input().split())
        s += x*y
    print('#'+str(test_case),"{:.6f}".format(s))
        
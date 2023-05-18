# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq
# [D2] 2007.패턴 마디의 길이

T = int(input())
for test_case in range(1, T + 1):
    s = str(input())
    n = s[0]
    s = s[1:]
    while True:
        p = s.index(n)
        n = n + s[0:p]
        s = s[p:]
        if n == s[0:len(n)]:
            break
    print('#'+str(test_case), len(n))
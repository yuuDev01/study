# 출처  https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PwGK6AcIDFAUq
import math

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for i in range(1, T + 1):
    n, m = map(int, input().split())
    hap = []
    k = 0
    for j in range(n):
        a, b, c = map(int, input().split())
        hap.append(a * 0.35 + b * 0.45 + c * 0.2)
        if j == m - 1:
            k = hap[-1]
    hap.sort(reverse=True)
    k = hap.index(k)
    s = math.trunc((k/(n/10)))
    print('#'+str(i),grade[s])
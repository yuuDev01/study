# 출처 https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWXGEbd6cjMDFAUo&categoryId=AWXGEbd6cjMDFAUo&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=17


import math

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    TC = []
    for _ in range(N):
        S = int(input())
        TC.append(S)
    # 건초더미 S의 요소 중 평균값보다 작은 요소 더하는 횟수 구하기
    a = sum(TC)/N
    answer = 0
    for i in TC :
        if i < a :
            answer += math.ceil(a - i)
    print('#'+str(test_case), answer)

    
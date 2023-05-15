# 1859. 백만 장자 프로젝트
# https://swexpertacademy.com/main/code/problem/problemSubmitDetail.do
T = int(input())
for i in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    profit = 0
    max = data[-1]
    for j in range(len(data)-2, -1, -1):
        if data[j] > max :
            max = data[j]
        else :
            profit += max - data[j] 
    print('#'+str(i), profit)
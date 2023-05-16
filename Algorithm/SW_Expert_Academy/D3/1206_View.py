# 출처 :https://swexpertacademy.com/main/code/problem/problemSubmitHistory.do?contestProbId=AV134DPqAA8CFAYh
# 1206. [S/W 문제해결 기본] 1일차 - View

T = 10 #테스트케이스
for test_case in range(1, T+1):
    answer = 0
    N = int(input()) # 건물의 개수 N
    NH = list(map(int, input().split())) # 건물 높이 리스트에 저장
    for i in range(2 , len(NH)-2):
        high = [NH[i-2], NH[i-1], NH[i+1], NH[i+2]]
        if NH[i] > max(high):
            answer += NH[i]-max(high)
    print('#'+str(test_case), answer)



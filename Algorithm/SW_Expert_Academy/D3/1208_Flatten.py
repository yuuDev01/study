# 1. 상자 높이값 리스트에서 가장 큰 값(max)과, 작은 값(min)을 가져와 각 +-1를 해준다
# 2. 덤프 횟수만큼 반복
# 3. 반복문이 끝나고 max, min값 차 구하기
T = 10
for test_case in range(1, T+1):
    N = int(input()) # 덤프 횟수
    boxs = list(map(int, input().split())) # 상자높이
    minV, maxV = 0,0
    for _ in range(N):
        minV = boxs.index(min(boxs))
        maxV = boxs.index(max(boxs))
        boxs[minV]+=1
        boxs[maxV]-=1
    print('#'+str(test_case),max(boxs)-min(boxs))

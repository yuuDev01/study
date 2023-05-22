# 3314. 보충학습과 평균
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBnA2jaxDsDFAWr


T= int(input())
for test_case in range(1, T+1):
    score = list(map(int, 
    input().split()))
    for i in range(len(score)):
        if score[i] < 40 :
            score[i] = 40
    print('#'+str(test_case), sum(score)//len(score))
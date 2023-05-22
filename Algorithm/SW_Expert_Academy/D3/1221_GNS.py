# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14jJh6ACYCFAYD
# 1221. GNS

numbers = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
numbers2 = { y:k for k,y in numbers.items()}

T = int(input())
for _ in range(T):
    n,m = map(str, input().split())
    print(n)
    m = int(m)
    mlist = list(map(str, input().split()))
    newlist = []
    for i in mlist:
        newlist.append(numbers.get(i))
        newlist.sort()
    for i in newlist:
        print(numbers2.get(i), end=' ')



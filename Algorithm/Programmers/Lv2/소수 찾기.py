# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 소수 찾기

numbers = []
def Permutation(array, depth, n, k):
  # array 배열 depth 깊이 n:배열길이 k뽑아낼 숫자개수
    if depth == k:  # 뽑아낼 숫자개수만큼 깊이
        numbers.append(int(''.join(array[:k])))
    for i in range(depth, n):
        array[depth], array[i] = array[i], array[depth]
        Permutation(array, depth + 1, n, k)
        array[depth], array[i] = array[i], array[depth] # 배열 되돌리기

def PrimeN(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def solution(number):
    array = list(number)
    for i in range(1,len(array)+1):
        Permutation(array, 0, len(array), i)
    s = set(numbers)
    
    #소수 구하기
    cnt = 0
    for i in s:
        if i == 0 or i == 1:
            continue
        if PrimeN(i):
            cnt+=1    
    return cnt
# 1 재귀 함수
def recursive_fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)



# 2 일반 함수
def fib(n) : 
    a, b = 1,1
    if n = 0 :
        return 0
    else n == 1 of n ==2 :
        return 1
    
    for i in range(1,n):
        a, b = b, a+b
    
    return a
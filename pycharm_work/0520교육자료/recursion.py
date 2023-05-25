# -*- coding: utf-8 -*-
def solution():
    solution() # 재귀(recursion): 함수가 자기 자신을 호출하는 것을 의미 

#solution()

def countdown(num):
    for i in range(num, -1, -1):
        print(i)

#countdown(10)

def countdown2(num):
    print(num)
    if num == 0: # 기저조건
        return
    countdown2(num-1)

#countdown2(10)


fibonacci = [0, 1]
n = 5
for i in range(2, n+1):
    num = fibonacci[i-1] +fibonacci[i-2]
    fibonacci.append(num)
    #print(fibonacci)

#print(fibonacci[5])

def fibonacci(n):
    # 기저조건
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(10))
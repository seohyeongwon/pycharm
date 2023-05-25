# -*- coding: utf-8 -*-

s = "(())()("

def solution(s):
    stack = []
    for b in s: #O(N)
        if b == "(":
            stack.append(b) #열린괄호를 저장 O(1)
        else: # ")" 닫힘괄호가 나올 때 
            if stack == []: # stack이 비어있는 상황(열리지 않았는데 닫힘 or 다 짝지어졌는데 닫힘이 또 들어옴)
                return False
            else: 
                stack.pop() # 리스트의 맨 끝 데이터를 제거 O(1)

    if stack != []:
        return False
    else:
        return True
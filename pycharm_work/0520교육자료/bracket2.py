# -*- coding: utf-8 -*-
p = "(()))("

def divide(p):
    open_b = 0
    close_b = 0
    for i in range(len(p)):
        if p[i] == '(':
            open_b += 1
        else:
            close_b += 1
        
        if open_b == close_b:
            u =  p[0:i+1]
            v = p[i+1::]       
            return u, v 

def chk(s):
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

p = "(()))("
# u = "(())" v=")("

# v=")("
# u = ")(" v=""
# "()"
def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if p == '': # 기저조건
        return p 
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    u, v = divide(p)
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    if chk(u):
        #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        return u + solution(v) # "(())" + "()" = "(())()"
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    else:
        #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        answer = '('
        #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        answer += solution(v) 
        #   4-3. ')'를 다시 붙입니다. 
        answer += ')'
        #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        for b in u[1:len(u)-1]: # 0번째, 마지막 인덱스 제외. 마지막인덱스: len(u)-1
            if b == '(':
                answer += ')'
            else:
                answer += '('
        #   4-5. 생성된 문자열을 반환합니다.
        return answer

print(solution(p))
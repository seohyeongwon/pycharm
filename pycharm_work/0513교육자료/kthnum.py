# -*- coding: utf-8 -*-

array = [1,5,2,6,3,7,4]
commands = [[2,5,3], [4,4,1], [1,7,3]]

def solution(array, commands):
    answer = [] 

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        #i, j, k = command[0], command[1], command[2]
        newArray = array[i-1:j] # i번째 ~ j번째 => i-1 인덱스 ~ j-1인덱스
        # newArray.sort()
        answer.append(sorted(newArray)[k-1]) # O(N*logN)
    
    return answer


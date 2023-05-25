# -*- coding: utf-8 -*-
def binary_search(array, value):
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2
        midvalue = array[midpoint]

        if midvalue == value: 
            return midpoint
        elif midvalue > value:  
            upper_bound = midpoint - 1
        elif midvalue < value:
            lower_bound = midpoint + 1

    return lower_bound

def solution(citations):
    # 정렬 
    citations.sort() #원본배열을 정렬 
    length = len(citations)

    i = 0
    h = 0
    while i <= length: # i=> h값의 후보. h값을 찾을때까지 length까지 반복 
        # h 이상 인용된 논문의 수 -> element의 값이 h 이상이다 -> 어떤 element가 h값? -> h값의 인덱스? 
        cand = binary_search(citations, i)

        if (length-1) - cand + 1 >= i:
            h = max(h, i) # 현재 후보와, 기존 후보 중 큰 값을 선택(최댓값을 찾아야하므로)

        i+=1
    
    return h
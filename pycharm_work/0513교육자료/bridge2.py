# -*- coding: utf-8 -*-
from collections import deque

bridge_length = 2
max_weight = 10
truck_weights = [7,4,5,6]

def solution(bridge_length, max_weight, truck_weights):
    time = 0
    total_weight = 0
    bridge = deque([0]*bridge_length)
    truck_weights.reverse() # 첫번째 대기 트럭이 맨 마지막 인덱스에 위치 #O(N)

    while truck_weights: #O(N)
        total_weight -= bridge.popleft() #O(1)

        if total_weight + truck_weights[-1] > total_weight :
            bridge.append(0) #O(1)
        else:
            truck = truck_weights.pop() #O(1)
            bridge.append(truck)#O(1)
            total_weight += truck

        time += 1

    return time + bridge_length
# O(N) + O(N) = O(2N) -> O(N)

    
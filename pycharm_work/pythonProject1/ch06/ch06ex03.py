bridge_length=2
max_weight=10
truck_weights=[7,4,5,6]

def solution(bridge_length, max_weight, truck_weights):
    time = 0#시간
    total_weight=0 #다리 위에 올라간 트럭 무게의 총합
    bridge=[0]*bridge_length #다리

#모든 트럭 통과때까지 반복
    while len(truck_weights)>0:
    #다리에 올라간 트럭 빠져나감
        tmp = bridge.pop(0)
    #트럭이 다리에 올라감
        total_weight = total_weight - tmp
    #트럭 다리 >다리 트럭 총합 + 대기 1번 트럭
        if total_weight + truck_weights[0]> max_weight:
        #time +=1
            bridge.append(0)
        else:
            truck=truck_weights.pop(0)
            bridge.append(truck)
            total_weight= total_weight+ truck #총무게에 다리에 올라간 트럭 무게를 더해
        #time+=1
        time+=1 #시간 증가

    time+=bridge_length#마지막 트럭 갈때까지 걸리는 시간
    return  time
print(truck_weights)
print(bridge)
#0(n^2)
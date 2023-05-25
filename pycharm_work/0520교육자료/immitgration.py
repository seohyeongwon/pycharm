n = 6
times = [7, 10]

def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times)*n # 최대 소요시간
    while left <= right:
        mid = (left + right) // 2

        chk = 0 # mid 시간동안 심사받은 사람의 총 수 
        for time in times:
            chk += mid // time

            if chk >= n: # 모든 심사관을 거치지 않더라도 mid시간동안 n명 이상이 심사를 받을 수 있다면 더 볼 필요가 없음 
                break
            
        if chk >= n: # 심사한 사람의 총 수가 심사 받아야할 수(n)보다 같거나 많은 경우
            answer = mid # 후보값으로 업데이트(갱신)
            right = mid - 1
        else:
            left = mid + 1

    return answer
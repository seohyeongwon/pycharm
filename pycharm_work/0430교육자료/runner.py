# https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    for c in callings: #O(N)
        idx = players.index(c) #O(N)
        players[idx-1], players[idx] = players[idx], players[idx-1]

    return players 

def solution(players, callings):
    player_dict = {}
    idx_dict = {}
    for i in range(len(players)): # O(N)
        player_dict[players[i]] = i 
        idx_dict[i] = players[i]

    for c in callings: #O(N)
        cur_player = c
        cur_idx = player_dict[c] #O(1)  
        
        front_idx = cur_idx - 1 
        front_player = idx_dict[front_idx] #O(1)

        player_dict[cur_player], player_dict[front_player] = front_idx, cur_idx 
        idx_dict[cur_idx], idx_dict[front_idx] = front_player, cur_player

    return list(idx_dict.values())


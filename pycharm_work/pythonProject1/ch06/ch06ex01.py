players = ["mumu","soe","poe","kai","mine"]
callings = ["kai","kai","mine","mine"]

# for i in range(len(callings)):
#      player = callings[i]
#
#      idx = players.index(player)
#
#      players[idx-1], players[idx] = players[idx], players[idx-1]
#      print(players)
#
# def solution(players, callings):
#     for c in callings:
#         idx = players.index(c)
#         players[idx - 1], players[idx] = players[idx], players[idx - 1]
#     return players

players = ["mumu","soe","poe","kai","mine"]

player_dict = {}
for i in range(len(players)):
    player_dict[players[i]]=[i]

print(player_dict)

idx_dict={}
for i in range(len(players)):
    idx_dict[i]= players[i]
print(idx_dict)

for c in callings:
    cur_player = c#현재 이름
    cur_idx = player_dict[c]#현재 등수

    #앞 선수의 정보 가져오기
    front_idx = cur_idx - 1 #앞선수 등수
    front_player = idx_dict[front_idx] #앞 이름

    #두선수 정보 바꿔치기

    player_dict[cur_player], player_dict[front_player] = front_idx, cur_idx#등 정보 바꾸기
    idx_dict[cur_idx], idx_dict[front_idx] = front_player, cur_player#선수명 바꾸기

#return list(idx_dict.values())

print(player_dict)
print(idx_dict)
print(list(idx_dict.values()))

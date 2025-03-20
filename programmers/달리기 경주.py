def solution(players, callings):
    """
    player=1등부터 현재 등수 순서대로 담긴 문자열 배열
    callings=해설진이 부른 이름을 담은 문자열 배열
    생각을 해보자 callings가 발동되면 호출된 선수와 호출된
    선수앞 선수의 리스트 번호를 바꾸면 되는게 아닐까
    1등은 어차피 안부른다
    """
    # for i in range(len(callings)):#callings 전부다 확인
    #     for j in range(len(players)):#players
    #         if players[j]==callings[i]:
    #             players[j-1],players[j]=players[j],players[j-1]
    #             continue
    #================================================================
    player_index = {player: idx for idx, player in enumerate(players)}
    for call in callings:
        curr_index=player_index[call]
        players[curr_index],players[curr_index-1]=players[curr_index-1],players[curr_index]
        player_index[players[curr_index]]=curr_index
        player_index[players[curr_index-1]]=curr_index-1

    return players
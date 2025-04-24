def solution(park, routes):
    #시작 위치 s 확인
    for row in range(len(park)):
        for col in range(len(park[0])):
            if park[row][col]=='S':
                start=(row,col)
                break
    #동서남북 방향 설정
    direction={
        'N':(-1,0),
        'S':(1,0),
        'W':(0,-1),
        'E':(0,1)
    }
    #현재위치값
    x,y=start
    #routes실행
    for route in routes:
        dir,dist=route.split()
        dist=int(dist)
        #이동전 위치를 저장
        nx,ny=x,y
        valid_move=True

        for _ in range(dist):
            nx += direction[dir][0]
            ny += direction[dir][1]

            #park, routes 에서 벗어나거나 장애물X에 이동될시 이동X
            if nx<0 or ny<0 or nx>=len(park) or ny>=len(park[0]) or park[nx][ny]=='X':
                valid_move=False
                break

        if valid_move:
            x,y=nx,ny

    return [x,y]
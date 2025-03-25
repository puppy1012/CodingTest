def solution(park, routes):
    # 공원의 크기
    rows = len(park)
    cols = len(park[0])

    # 시작 위치 찾기
    for r in range(rows):
        for c in range(cols):
            if park[r][c] == 'S':
                start = (r, c)
                break

    # 방향 설정 (북, 남, 서, 동)
    direction = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }

    # 현재 위치
    x, y = start

    # 명령 수행
    for route in routes:
        dir, dist = route.split()
        dist = int(dist)

        # 이동 전 위치 저장
        nx, ny = x, y
        valid_move = True

        for _ in range(dist):
            nx += direction[dir][0]
            ny += direction[dir][1]

            # 경계 밖이거나 장애물이 있는 경우 이동 실패
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or park[nx][ny] == 'X':
                valid_move = False
                break

        # 유효한 이동이면 위치 갱신
        if valid_move:
            x, y = nx, ny

    return [x, y]
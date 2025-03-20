from collections import deque
n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#출구는 입력받는 n,m위치에 존재
#이동할때마다 이동값 +1, 시작,도착점까지 포함
result=0
#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y) :
    #큐 구현을 위한 deque
    queue = deque()
    #while문 실행용, 현재 위치 저장용
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if nx<0 or ny<0 or nx>= n or ny >=m:
                print('nx',x,'ny',y,'값은 벗어나는값이다')
                continue
            if graph[nx][ny]==0 :
                print('nx', x, 'ny', y, '값은 벽이다')
                continue
            if graph[nx][ny] ==1 :
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
                print(queue)

    return graph[n-1][m-1]
#시작 위치점 입력
print(bfs(0,0))

"""
5 6
101010
111111
000001
111111
111111
"""
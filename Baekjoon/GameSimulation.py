n,m = map(int,input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화한다
d=[[0]*m for _ in range (n)]
print('d:',d)
#현재 캐릭터의 X좌표, Y좌표 ,방향을 입력받기
x,y,direction = map(int,input().split())
#현재 좌표 방문 처리
d[x][y]=1
#전체 맵 정보를 입력받는다
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))
#북동남서 방향을 정의
dx=[-1,0,1,0]
dy=[0,1,0,-1]
#왼쪽으로 회전

def turn_left():
    global direction
    direction -=1
    if direction ==-1:
        direction=3
#direction 값은 0123으로 존재
#0 북쪽값에서 -1이될시 서쪽값3으로 이동하게 설정
count=1
turn_time=0
while True :
    turn_left()
    #turn_left를 실행하여 direction의 값을 변환
    nx= x+dx[direction]
    ny= y+dy[direction]
    #nx,y값을 입력받은 x,y값 + direction의 방향에 따른 값을 대입하여 입력
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        #d= 가본적이 있는지 확인용 리스트
        #array= 육지,바다 체크 육지일시 0 바다일시 1
        #둘다 조건이 충족될시 d의 리스트에 가봤다 입력1
        #x와 y의 값을 nx,y을 대입하여 이동시킴
        #count+1
        #새로운칸이니까 turn_time을 0으로 초기화
        #아래조건문은 볼필요가 없으니 continue
        d[nx][ny]=1
        x= nx
        y = ny
        count +=1
        turn_time=0
        continue
    #회전하고 정면에 가보지 않은 칸이 없거나 바다인경우일때
    else :
        # 위의 turn_left를 실행했지만 안되었으니까 turn_time만 증가
        turn_time+=1

    #네 방향 모두 이동하지 못할때
    #4번 돌았을때
    if turn_time ==4:
        #현재 위차 x - 현재 마지막으로 향한 방향값dx[direction]값을 뺀다
        nx = x-dx[direction]
        ny = y-dy[direction]
        #이후 array(육지,바다확인용 리스트)의 nx,ny번째 포인트값이 0(육지)이라면
        if array[nx][ny] == 0:
            x= nx
            y= ny
            #x,y값에 nx,ny값을 대입한다
        else:
            #아니면 break해서 while문을 탈출하라
            break
        turn_time=0
        #이건 뭐지

print(count)
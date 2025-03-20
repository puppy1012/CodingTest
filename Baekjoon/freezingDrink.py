n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    print('dfs(',x,',',y,')실행')
    #테이블을 벗어나는 값이 존재할시 Fasle 반환
    if x<=-1 or x>=n or y<=-1 or y>=m:
        print('잘못된값 False값 반환됨')
        return False
    #구멍이 뚫려져있는곳0이라면 칸막이1로 변경
    #return True로 되어있는 이유는 크기에 상관없이 얼음을 만들수 있으므로 뭉쳐져 있는 부분을 확인 후
    #중복값을 막기위해 칸막이로 막는다
    #이후 얼음을 만들수있다는 결과값을 반환하기위함

    if graph[x][y] == 0:
        graph[x][y]=1
        #인근값을 확인
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        print('dfs',x,',',y,'번째 True값 반환됨')
        return True
    print('dfs',x,',',y,'= 칸막이 존재 False 반환')
    return False

result=0
for i in range(n):
    for j in range(m):
        #반환값이 True라면 result값 증가
        if dfs(i,j)==True:
            result +=1
            print('result=',result)

print(result)
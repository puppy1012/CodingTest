"""
stack=[]
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])

from collections import deque

queue =deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
print(queue)
queue.reverse()
print(queue)

def recursive_function(i):
    if i==100:
        return
    print(i,'번째 재귀 함수에서', i+1,'번째 재귀함수를 호출합니다')
    recursive_function(i+1)
    print(i,'번째 재귀 함수를 종료합니다')

recursive_function(1)

#반복적으로 구현한 n!
def factorial_iterative(n):
    result =1
    for i in range(1,n+1): result *=i
    return result

#재귀적으로 구현한 n!
def factorial_recursive(n):
    if n<=1: return 1
    #n! = n*(n-1)!
    return n* factorial_recursive(n-1)
print('반복적 구현:',factorial_iterative(5))
print('재귀적으로구현:',factorial_recursive(5))

INF=9999999
graph1=[
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
print(graph1)

graph=[[]for _ in range(3)]
print(graph)
graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))

print(graph[0])
"""
def dfs(graph,v,visited):
    visited[v]=True#방문했다 표시
    print(v,end='\n')
    for i in graph[v]:
        print('graph의 ',i,'번째 차례')
        if not visited[i]:
            #print('not visitied=',visited[i])
            #print(visited)
            dfs(graph,i,visited)

graph=[
    [],#0번 노드
    [2,3,8],#1번 노드에 인접한 노드값
    [1,7],#2번 노드에 인접한 노드값
    [1,4,5],#3번 노드에 인접한 노드값
    [3,5],#4번 노드에 인접한 노드값
    [3,4],#5번 노드에 인접한 노드값
    [7],#6번 노드에 인접한 노드값
    [2,6,8],#7번 노드에 인접한 노드값
    [1,7]#8번 노드에 인접한 노드값
]
visited=[False]*9#방문확인용 리스트
#print('graph=',graph)
#print('visited=',visited)
#dfs(graph,1,visited)#dfs의 1번부터 방문하겠다

from collections import deque

def bfs(graph,start,visited):
    queue=deque([start])
    print(queue)
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end='')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


bfs(graph,1,visited)
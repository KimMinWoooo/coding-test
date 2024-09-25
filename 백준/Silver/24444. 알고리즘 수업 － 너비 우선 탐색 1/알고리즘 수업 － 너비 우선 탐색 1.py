import sys
from collections import deque

N,M,R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

# 입력받는 간선 정보 그래프화 시키기
for i in range(M):
    TL = list(map(int, sys.stdin.readline().split()))
    graph[TL[0]].append(TL[1])
    graph[TL[1]].append(TL[0])

# 정렬
for i in range(N+1):
    graph[i].sort()

# bfs
def bfs(graph, R, visited):
    queue=deque([R])
    visited[R]=1
    count=2

    while queue:
        R = queue.popleft()
        for i in graph[R]:
            if visited[i] == 0:
                queue.append(i)
                visited[i]=count
                count+=1
# 정점 배열
visited=[0]*(N+1)
bfs(graph, R, visited)
for i in visited[1::]:
    print(i)
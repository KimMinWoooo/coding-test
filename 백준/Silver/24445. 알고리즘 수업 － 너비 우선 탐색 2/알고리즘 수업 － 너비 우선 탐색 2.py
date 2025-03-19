import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

q = deque()
q.append(R)
order = 1
while len(q) > 0:
    node = q.popleft() # 1
    visited[node] = True # 1을 방문했다!
    result[node] = order
    order += 1
    for next in graph[node]:
        if visited[next] == True: # 이미 방문했으면 지나감
            continue
        visited[next] = True
        q.append(next) # 다음거 방문



for i in range(1, N+1):
    print(result[i])
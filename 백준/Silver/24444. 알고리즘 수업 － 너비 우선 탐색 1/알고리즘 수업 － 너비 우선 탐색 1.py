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
    graph[i].sort()

q = deque()
q.append(R)
order = 1
while len(q) > 0:
    node = q.popleft()
    visited[node] = True
    result[node] = order
    order += 1
    for next in graph[node]:
        if visited[next] == True:
            continue
        visited[next] = True
        q.append(next)



for i in range(1, N+1):
    print(result[i])
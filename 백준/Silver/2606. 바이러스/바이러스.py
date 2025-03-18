from collections import deque

N = int(input())
M = int(input())

gh = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    gh[a].append(b)
    gh[b].append(a)

q = deque()

q.append(1)

while len(q) > 0:
    node = q.popleft() # 1
    visited[node] = 1 # 1을 방문했다!

    for next in gh[node]:
        if visited[next] == 1: # 이미 방문했으면 지나감
            continue
        q.append(next) # 다음거 방문

print(sum(visited) - 1)
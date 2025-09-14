import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

N, M, R = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
count = 1
for _ in range(M):
    A, B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(N+1):
    graph[i].sort()

def dfs(R):
    global count
    visited[R] = count
    count += 1
    for nxt in graph[R]:
        if visited[nxt] == 0:
            dfs(nxt)

dfs(R)

for i in range(1, N + 1):
    print(visited[i])
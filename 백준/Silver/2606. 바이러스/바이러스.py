
N = int(input())
M = int(input())

gh = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    gh[a].append(b)
    gh[b].append(a)

def recur(node):
    visited[node] = 1

    for next in gh[node]:
        if visited[next] == 1:
            continue
        recur(next)


recur(1)
print(sum(visited)-1)
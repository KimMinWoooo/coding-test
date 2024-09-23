
n, m, v = map(int, input().split())

#그래프 제작
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

vsted1 = [0]*(n+1)
vsted2 = vsted1.copy()

def dfs(v): # 스택을 사용해서 dfs를 해결해보기 , 스택은 후입선출 방식이다.
    vsted1[v] = 1 # 방문 처리를 하자
    print(v, end=' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and vsted1[i] == 0:
            dfs(i)


def bfs(v): # queue를 사용해서 bfs를 해결해보기 , 큐는 선입선출 방식이다.
    queue = [v]
    vsted2[v] = 1 # 방문 처리를 하자
    while queue:
        v = queue.pop(0) # 큐는 선입선출 방식이기에 방문한 곳을 삭제를 해주고 시작
        print(v, end=' ')
        for i in range(1, n+1):
            if (vsted2[i] == 0 and graph[v][i] == 1):
                queue.append(i)
                vsted2[i] = 1

dfs(v)
print()
bfs(v)
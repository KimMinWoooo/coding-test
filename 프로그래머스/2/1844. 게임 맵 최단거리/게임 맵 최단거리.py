from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    while q:
        ex, ey = q.popleft()
        
        for dx,dy in[[1,0],[-1,0],[0,1],[0,-1]]:
            nx,ny = ex+dx, ey+dy
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    if maps[nx][ny] == 1:
                        visited[nx][ny] = 1
                        q.append([nx,ny])
                        maps[nx][ny] = maps[ex][ey] + 1
    if maps[n-1][m-1] == 1:
        return -1
    return maps[n-1][m-1]
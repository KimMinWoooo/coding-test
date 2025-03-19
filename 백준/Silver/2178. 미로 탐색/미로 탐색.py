import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N):
    row = list(map(int,input().strip()))
    arr.append(row)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
q.append((0,0))

while len(q) > 0:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if arr[nx][ny] == 0:
            continue

        if arr[nx][ny] == 1:
            arr[nx][ny] = arr[x][y] + 1
            q.append((nx,ny))

print(arr[N-1][M-1])

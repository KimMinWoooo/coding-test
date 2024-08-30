import sys 
from collections import deque
input = sys.stdin.readline

n = int(input())
ball = deque(list(map(int,input().split())))
index = deque({i for i in range(1, n+1)})
result = []

while ball:
    number = ball.popleft()
    result.append(index.popleft())
    if number > 0:
        ball.rotate(-(number-1))
        index.rotate(-(number-1))
    else:
        ball.rotate(-number)
        index.rotate(-number)
print(*result)

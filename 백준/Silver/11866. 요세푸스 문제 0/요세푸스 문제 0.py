import sys
from collections import deque
n, k = map(int, input().split())
#deq를 생성해서 방향을 돌아가는걸 지정해줌
deq = deque([i for i in range(1, n+1)])

# 순열 만들기
res = []
while len(deq) != 0:
    for _ in range(k-1):
        deq.append(deq.popleft())
    res.append(str(deq.popleft()))
print("<"+(", ".join(res))+">")
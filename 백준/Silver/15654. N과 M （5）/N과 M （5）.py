
def solution(K):
    if K == M:
        print(*result)
        return
    for i in range(N):
        if j[i] in result:
            continue
        result.append(j[i])
        solution(K+1)
        result.pop()
N, M = map(int, input().split())
j = list(map(int, input().split()))

j.sort()
result = []
solution(0)
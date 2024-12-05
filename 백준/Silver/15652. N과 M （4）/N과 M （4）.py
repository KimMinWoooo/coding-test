def solution(S, K):
    if K == M:
        print(*result)
        return
    for i in range(S, N+1):
        result.append(i)
        solution(i,K+1)
        result.pop()

N, M = map(int, input().split())

result = []

solution(1, 0)
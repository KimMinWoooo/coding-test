def solution(S, K):
    if K == M:
        print(*result)
        return
    for i in range(S, N+1):
        if i in result:
            continue
        result.append(i)
        solution(i + 1, K + 1)
        result.pop()

N, M = map(int, input().split())

result = []

solution(1, 0)
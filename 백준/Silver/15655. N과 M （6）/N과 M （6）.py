
def solution(S, K):
    if K == M:
        print(*result)
        return
    for i in range(S, N):
        if j[i] in result:
            continue
        result.append(j[i])
        solution(i+1,K+1)
        result.pop()
N, M = map(int, input().split())
j = list(map(int, input().split()))

j.sort()
result = []
solution(0, 0)
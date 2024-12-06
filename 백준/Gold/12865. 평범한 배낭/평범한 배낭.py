# 탑 바텀 dp로 푼 넵섹 문제

import sys
input = sys.stdin.readline

def recur(idx, weight):
    if weight > K:
        return -99999999
    if idx == N:
        return 0
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    dp[idx][weight] = max(recur(idx+1, weight + arr[idx][0])+ arr[idx][1], recur(idx+1, weight))

    return dp[idx][weight]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(100_001)] for _ in range(N)]

ans = recur(0, 0)
print(ans)
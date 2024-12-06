# 바텀 업 dp 넵섹 문제
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
item = []
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for idx in range(1, N+1):
    x, y = map(int, input().split())
    for weight in range(1, K+1):
        if weight < x:
            dp[idx][weight] = dp[idx-1][weight]
        else:
            dp[idx][weight] = max(dp[idx-1][weight], dp[idx-1][weight-x] + y)
print(dp[N][K])
# 바텀 업 dp 

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

for idx in range(n)[::-1]:
    if idx + arr[idx][0] > n:
        dp[idx] = dp[idx+1]
    else:
        dp[idx] = max(dp[idx + arr[idx][0]]+arr[idx][1], dp[idx+1])


print(max(dp))
import sys
input = sys.stdin.readline
T = int(input())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
#dp[4] = 7
#dp[5] = 13
#dp[6] = 24
# dp[i-1] + dp[i-2] + dp[i-3] = dp[i]
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] # 점화식
for i in range(0, T):
    dpNum = int(input())
    print(dp[dpNum])

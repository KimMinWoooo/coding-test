import sys
sys.setrecursionlimit(10**6)

def recur(y, x):
    if dp[y][x] != 0:
        return dp[y][x]
    
    for dy, dx in [[1, 0],[-1, 0],[0, 1],[0, -1]]:
        ey = y+dy
        ex = x+dx

        if 0 <= ex < n and 0 <= ey < n:
            if arr[y][x] < arr[ey][ex]:
                dp[y][x] = max(dp[y][x], recur(ey,ex) + 1)
    return dp[y][x]



import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
for y in range(n):
    for x in range(n):
        recur(y, x)

print(max(map(max, dp))+1)
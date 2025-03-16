import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
X = int(input())

s = 0
e = N-1
ans = 0

while s < e:
    if arr[s] + arr[e] < X:
        s += 1
    elif arr[s] + arr[e] > X:
        e -= 1
    else:
        ans += 1
        e -= 1
print(ans)
N = int(input())
arr = list(map(int, input().split()))

pre = [-1000 for _ in range(N+1)]

for i in range(N):
    pre[i+1] = max(pre[i] + arr[i], arr[i])

print(max(pre))
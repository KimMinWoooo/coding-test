A, B = map(int, input().split())
arr = list(map(int, input().split()))

pre = [0 for _ in range(A+1)]

for i in range(A):
    pre[i+1] = pre[i]+arr[i]

ans = []
for k in range(B, A+1):
    ans.append(pre[k] - pre[k-B])

print(max(ans))
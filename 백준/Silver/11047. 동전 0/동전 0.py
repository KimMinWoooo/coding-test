import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst_a = []
cnt = 0
for _ in range(n):
    lst_a.append(int(input()))
lst_a.sort(reverse=True)
for i in lst_a:
    if k == 0:
        break
    if i <= k:
        cnt += k // i
        k %= i
print(cnt)
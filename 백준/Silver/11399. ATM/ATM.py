import sys
input = sys.stdin.readline
N = int(input())
lst_a = list(map(int, input().split()))
lst_a.sort() # [1, 2, 3, 3, 4] 
cnt = 0
for i in range(1, N+1):
    cnt += sum(lst_a[0:i])
print(cnt)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
sums = [0]
mysum = 0

for i in range(n):
  mysum += num[i]
  sums.append(mysum)


for i in range(m):
  a, b = map(int, input().split())
  print(sums[b] - sums[a-1])

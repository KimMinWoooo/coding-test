import sys
input = sys.stdin.readline
N = int(input())
a = []
for i in range(N):
    k = int(input())
    a.append(k)
a.sort(reverse=False)
for j in a:
    print(j)
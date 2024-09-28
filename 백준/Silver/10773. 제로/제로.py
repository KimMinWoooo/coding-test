
import sys
input = sys.stdin.readline
N = int(input())
lst = []
result = 0
for i in range(N):
    k = int(input())
    if lst and k == 0:
        lst.pop()
    else:
        lst.append(k)
print(sum(lst))

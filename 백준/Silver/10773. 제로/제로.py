import sys
input = sys.stdin.readline
N = int(input())

stack = []
for i in range(N):
    K = int(input())
    if K == 0:
        stack.pop()
    else:
        stack.append(K)

print(sum(stack))

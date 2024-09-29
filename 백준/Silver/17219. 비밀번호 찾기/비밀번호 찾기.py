import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dics = {}
for _ in range(n):
    a, b = input().split()
    dics[a] = b
for _ in range(m):
    print(dics[input().rstrip()])

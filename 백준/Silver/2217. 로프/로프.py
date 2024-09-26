import sys
N = int(sys.stdin.readline())
m = []

for i in range(N):
    m.append(int(sys.stdin.readline()))

m.sort(reverse=True)
res = []
for j in range(N):
    res.append(m[j]*(j+1))

print(max(res))
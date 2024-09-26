N = int(input())
m = []

for i in range(N):
    m.append(int(input()))

m.sort(reverse=True)
res = []
for j in range(N):
    res.append(m[j]*(j+1))

print(max(res))
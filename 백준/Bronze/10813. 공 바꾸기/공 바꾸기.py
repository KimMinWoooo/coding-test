N, M = map(int,input().split())
pack = list(range(1, N+1))

for _ in range(M):
    i, j = map(int,input().split())
    pack[i-1], pack[j-1] = pack[j-1], pack[i-1]
print(*pack)
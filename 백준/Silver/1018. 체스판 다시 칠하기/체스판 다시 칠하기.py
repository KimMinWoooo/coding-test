N, M = map(int, input().split())
chess = []
solve = []

for _ in range(N):
    chess.append(input())

for i in range(N-7):
    for j in range(M-7):
        dr1 = 0
        dr2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if chess[a][b] != 'B':
                        dr1 += 1
                    elif chess[a][b] != 'W':
                        dr2 += 1
                else:
                    if chess[a][b] != 'W':
                        dr1 += 1
                    elif chess[a][b] != 'B':
                        dr2 += 1
        solve.append(dr1)
        solve.append(dr2)
print(min(solve))
                
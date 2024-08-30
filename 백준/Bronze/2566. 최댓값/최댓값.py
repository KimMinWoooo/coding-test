pyo = []
for _ in range(9):
    row = list(map(int, input().split()))
    pyo.append(row)

maxNum = 0
maxRow, maxCol = 0, 0

for row in range(9):
    for col in range(9):
        if maxNum <= pyo[row][col]:
            maxRow, maxCol = row + 1 , col + 1
            maxNum = pyo[row][col]

print(maxNum)
print(maxRow, maxCol)
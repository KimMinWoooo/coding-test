
N = int(input())
cntA = 0
cntB = 0
result = list(input())
for i in range(len(result)):
    if result[i] == 'A':
        cntA += 1
    if result[i] == 'B':
        cntB += 1

if cntA > cntB:
    print('A')
elif cntA < cntB:
    print('B')
else:
    print('Tie')
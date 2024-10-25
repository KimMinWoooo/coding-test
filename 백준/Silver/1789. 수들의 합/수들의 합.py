S = int(input())
N = 0
result = 0
while True:
    result += 1
    N += result
    if N > S:
        break

print(result-1)
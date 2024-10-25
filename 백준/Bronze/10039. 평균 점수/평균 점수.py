import sys
input = sys.stdin.readline
result = 0
for i in range(0, 5):
    A = int(input())
    if A <= 40:
        result += 40
    else:
        result += A
print(result//5)
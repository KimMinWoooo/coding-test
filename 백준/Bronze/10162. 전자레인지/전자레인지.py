
N = int(input())
C = 0
B = 0
A = 0

if N >= 300:
    C = N // 300
    N = N % 300
if N >= 60:
    B = (N // 60)
    N = N % 60
if N >= 10:
    A = (N // 10)
if N % 10 != 0:
    print(-1)
else:
    print(C, B, A)
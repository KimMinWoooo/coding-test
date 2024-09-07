T = int(input())
M = []
for _ in range(T):
    k = int(input())
    # k * 23을 순서대로 저장해놔야함 -> list
    M.append(k*23)

for i in range(T):
    print(M[i])

from sys import stdin
def input():
    return stdin.readline().rstrip()
dic_id = {}
dic_name = {}
N, M = map(int, input().split())
for i in range(1, N + 1):
    pk = input()
    dic_id[i] = pk
    dic_name[pk] = i

for _ in range(M):
    qs = input()
    if qs.isdigit():
        print(dic_id[int(qs)])
    else:
        print(dic_name[qs])
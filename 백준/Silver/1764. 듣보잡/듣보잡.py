from sys import stdin
def input():
    return stdin.readline().rstrip()
n, m = map(int, input().split())
result = []
dic_lsn = set()
dic_see = set()
for i in range(n):
    dic_lsn.add(input())
for j in range(m):
    dic_see.add(input())

for i in dic_lsn:
    if i in dic_see:
        result.append(i)
result.sort()
print(len(result))
for i in result:
    print(i)
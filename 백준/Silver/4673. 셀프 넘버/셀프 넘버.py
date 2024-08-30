m = set(range(1, 10001))
g = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    g.add(i)

s = sorted(m - g)
for i in s:
    print(i)
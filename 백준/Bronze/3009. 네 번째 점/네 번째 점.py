import sys
input = sys.stdin.readline

c = []
s = []
for i in range(3):
    a, b = map(int, input().split())
    c.append(a)
    s.append(b)
for i in range(3):
    if c.count(c[i]) == 1:
        x = c[i]
    if s.count(s[i]) == 1:
        y = s[i]

print(x, y)

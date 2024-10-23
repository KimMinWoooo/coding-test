T = int(input())
for _ in range(T):
    lst = list(input().split(" "))
    rst = float(lst[0])
    for i in range(1, len(lst)):
        if lst[i] == '@':
            rst *= 3
        elif lst[i] == '%':
            rst += 5
        elif lst[i] == '#':
            rst -= 7
    print("%.2f" % rst)
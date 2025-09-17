def recur(num):
    if num == m:
        print(*arr)
        return
    for i in range(1, n+1):
        if i in arr:
            continue
        arr.append(i)
        recur(num+1)
        arr.pop()

n,m = map(int,input().split())
arr = []
recur(0)
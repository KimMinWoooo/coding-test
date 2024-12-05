def solution(number):
    if number == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if arr and arr[-1] == i:
            continue
        if i in arr:
            continue
        arr.append(i)
        solution(number + 1)
        arr.pop()


N, M = map(int, input().split())
arr = []

solution(0)

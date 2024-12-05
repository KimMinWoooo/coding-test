def recur(idx,p,f,s,v,c):
    global answer
    global use
    global ans_use

    if p >= mp and f >=mf and s >= ms and v >= mv:
        if answer > c:
            answer = min(answer, c)
            ans_use = []
            for i in use:
                ans_use.append(i)
    if idx == N:
        return
    
    # 식재료 합을 한 경우
    use.append(idx+1)
    recur(idx+1, p+foods[idx][0], f+foods[idx][1], s+foods[idx][2], v+foods[idx][3], c+foods[idx][4])
    use.pop()
    recur(idx+1,p,f,s,v,c)

N = int(input())

mp, mf, ms, mv = map(int, input().split())

foods = [list(map(int, input().split())) for _ in range(N)]

answer = 1e9
use = []
ans_use = []
recur(0,0,0,0,0,0)
if ans_use:
    print(answer)
    print(*ans_use)
else:
    print(-1)
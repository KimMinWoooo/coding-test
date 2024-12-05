def recur(idx, p,f,s,v,c):
    global answer
    global used
    global answer_used

    
    if mp <= p and mf <= f and ms <= s and mv <= v:
            if answer > c:
                answer = min(answer, c)
                answer_used = []
                for i in used:
                    answer_used.append(i)
    if idx == n:
        return

    used.append(idx+1)
    recur(idx + 1, p+foods[idx][0], f+foods[idx][1], s+foods[idx][2], v+foods[idx][3], c+foods[idx][4])
    used.pop()
    recur(idx + 1,p,f,s,v,c)
    

n = int(input())
mp,mf,ms,mv = map(int, input().split())
foods = [list(map(int, input().split())) for _ in range(n)]

answer = 1e9
used = []
answer_used = []
recur(0,0,0,0,0,0)

if answer_used:
    print(answer)
    print(*answer_used)
else:
    print(-1)

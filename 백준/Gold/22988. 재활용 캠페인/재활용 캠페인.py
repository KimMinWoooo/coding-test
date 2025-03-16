import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = sorted(list(map(int, input().split())))

s = 0
e = N-1
ans = 0
bs = 0

while s <= e:
    if arr[e] == X: # 제일 용량 많은 병이 이미 꽉찬 병이면
        ans += 1
        e -= 1
        continue
    if s == e: # 병 하나만 남았으면
        bs += 1
        break
    if arr[e] + arr[s] >= X/2: # 용량 2개의 합이 반 이상이면
        ans += 1
        e -= 1
        s += 1
    else: # 위 조건에 부합하지 않으면 작은 병은 그냥 남은 병으로 간주
        s += 1
        bs += 1

print(ans + bs//3)
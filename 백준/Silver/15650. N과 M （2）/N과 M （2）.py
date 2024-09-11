N, M = list(map(int,input().split()))
result = []

def dfs(start):
    # 조건 : 수열의 길이가 M개까지 골라졌다면
    if (len(result) == M):
        print(' '.join(map(str, result)))
        return
    # 반복 : start 부터 N + 1 까지
    for i in range(start, N + 1):
        # 조건 : result 수열안에 i가 없으면
        # result에 i를 추가하고 dfs를 추가 재귀 호출 -> 끝나면 마지막 숫자를 pop해서 제거함
        if i not in result:
            result.append(i)
            dfs(i + 1)
            result.pop()
dfs(1)
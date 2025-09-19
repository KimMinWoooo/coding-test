def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    def dfs(start_node):
        visited[start_node] = True
        for i in range(n):
            if computers[start_node][i] == 1 and not visited[i]:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
            
    return answer


# computer[i][j] -> i와 j가 연결되어있다 -> 2개에서 1개의 네트워크로 묶임
# computer[1] 번 네트워크 부터 연결되어있는 간선 (visited)를 찾고
# 간선이 어디와 연결되어있는지 체크함
# 1번과 2번이 연결되어있으면 2번에서 1번과 연결되어있다고 이미 체크 했으니 넘어감
# 3번은 아무와도 간선이 없다 = 외딴섬 네트워크로 + 1
# 이런식으로 그래프 탐색을 하면 될듯
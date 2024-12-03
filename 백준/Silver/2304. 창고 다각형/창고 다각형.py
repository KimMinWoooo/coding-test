n = int(input())

graph = [0]*10001
x_list = []
y_list = []

for i in range(n):
    x, y = map(int,input().split())
    # x 좌표의 y값을 대입함
    graph[x] = y
    x_list.append(x)
    y_list.append(y)

maxHeight = max(y_list) # 최고 Y 값
maxWidth = max(x_list)  # 가장 오른쪽 x
# 왼쪽 누적합 배열 생성
prefix = [0]*(maxWidth+2)
# 오른쪽 누적합 배열 생성
suffix = [0]*(maxWidth+2)

maxPoint = []

#prefix 계산 
# 왼쪽부터 최고 Y값이 있는 x까지 누적 합 구하기
h = 0
for f in range(1,maxWidth+3):
    # y값이 최고인 x까지 왔으면
    if(graph[f] == maxHeight):
        maxPoint.append(f)
        break # break
    # 그게 아니면 h와 f(x)좌표에 있는 y값 비교해서 누적합에 추가하라
    h = max(h, graph[f]) 
    prefix[f] = prefix[f-1] + h

# 오른쪽부터 최고 Y 값이 있는 x까지 누적 합 구하기
h = 0
for b in range(maxWidth,0,-1):
    if(graph[b] == maxHeight):
        maxPoint.append(b)
        break
    h = max(h, graph[b])
    suffix[b] = suffix[b+1] + h


#정답 합치기
# 최고 Y값이 있는 x기준 왼쪽(prefix) + 오른쪽(suffix) 더함
answer = max(prefix) + max(suffix)
# 최고 Y값이 있는 면적 추가 더함
answer += (maxPoint[1] - maxPoint[0] + 1 )*maxHeight

print(answer)

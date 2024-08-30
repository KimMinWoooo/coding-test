
N = int(input()) 
M = int(input()) # 만들어야 하는 수
lst = list(map(int, input().split()))

lst.sort()
start, end = 0, len(lst)-1 # start 가장 작은 수 지점, end 가장 큰 수 지점
cnt = 0 # start와 end의 합이 M이 되는 횟수

while start < end:
    answer = lst[start] + lst[end]
    if answer > M: # 두 수의 합이 M보다 크다는건 end값이 너무 크단 얘기
        end -= 1
    elif answer < M: # 두 수의 합이 M보다 작다는건 start값이 너무 작단 얘기
        start += 1
    else: # 위 두 경우가 아닌 경우? -> 합이 M와 같다는거 
        cnt += 1 # cnt 추가
        start += 1 # start 지점 증가
        end -= 1 # end 지점 증가
print(cnt)

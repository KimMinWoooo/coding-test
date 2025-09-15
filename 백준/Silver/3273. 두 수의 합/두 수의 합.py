import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
target = int(input())
result = 0
start=0
end = N-1

while start < end:
    if arr[start]+arr[end] > target:
        end -=1
    elif arr[start]+arr[end] < target: # 13 12
        start += 1
    else:
        result += 1
        end -= 1
print(result)
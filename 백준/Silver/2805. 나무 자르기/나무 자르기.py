import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))
left = 1
right = sum(trees)
while left <= right:
    mid = (left+right) // 2
    result = 0  
    for i in trees:
        if i > mid:
            result += i - mid
    if result >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)
import sys
input = sys.stdin.readline

N = int(input())
arr1 = sorted(list(map(int, input().split())))

M = int(input())
arr2 = list(map(int, input().split()))


for number in arr2:
    s = 0
    e = N-1
    flag = False

    while s <= e:
        mid = (s+e)//2
        if arr1[mid] < number:
            s = mid + 1
        elif arr1[mid] > number:
            e = mid - 1
        else: # arr1[mid] < number
            flag = True
            break

    print(1 if flag else 0, end=' ')
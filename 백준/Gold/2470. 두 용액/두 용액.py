import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

s = 0
e = N-1

ans = abs(arr[s] + arr[e])
res = [arr[s], arr[e]]

while s < e:
    s1 = arr[s]
    s2 = arr[e]
    sum = s1+s2
    if abs(sum) < ans:
        ans = abs(sum)
        res = [s1,s2]
        if ans == 0:
            break
    if sum < 0:
        s += 1
    else:
        e -= 1
print(res[0], res[1])
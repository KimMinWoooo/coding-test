def binary_sch(low, high):
    if high<low:
        return
    global n
    global res
    mid = (low+high)//2
    tmp = 0
    for i in lst:
        tmp += i//mid
    if tmp >= n:
        res=mid
        binary_sch(mid+1, high)
    else:
        binary_sch(low, mid-1)

k, n = map(int, input().split())
lst =[0]*k
for i in range(k):
    lst[i]=int(input())
big=max(lst)
res=0
binary_sch(0, big*2)
print(res)
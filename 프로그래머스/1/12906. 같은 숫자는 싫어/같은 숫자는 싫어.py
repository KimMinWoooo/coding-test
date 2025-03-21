def solution(arr) :
    ans = [arr[0]]
    for i in range(len(arr)):
        if arr[i] == ans[-1]:
            continue
        else:
            ans.append(arr[i])
    
    return ans
        
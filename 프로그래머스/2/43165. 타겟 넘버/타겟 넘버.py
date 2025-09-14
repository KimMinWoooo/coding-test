answer = 0

def dfs(numbers,target,value,idx):
    global answer
    
    if len(numbers) == idx:
        if value == target:
            answer += 1
        return
    
    dfs(numbers,target,value-numbers[idx],idx+1)
    dfs(numbers,target,value+numbers[idx],idx+1)
    
def solution(numbers, target):
    global answer
    dfs(numbers,target,0,0)
    return answer




def recur(idx, price):
    global result
    if idx > N: 
        return
    if idx > N-1:
        
        result = max(result, price)
        return
    
    
    recur(idx+inter[idx][0], price+inter[idx][1])
    recur(idx+1, price)

N = int(input())

inter = [list(map(int, input().split())) for _ in range(N)]
result = 0
recur(0, 0)
print(result)
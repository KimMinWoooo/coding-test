P = int(input())

for _ in range(P):
    N, M = map(int, input().split())
    printQ = list(map(int, input().split()))
    
    result = 1
    while printQ:
        if printQ[0] < max(printQ): 
            printQ.append(printQ.pop(0))

        else: 
            if M == 0: break

            printQ.pop(0) 
            result += 1 

        M = M - 1 if M > 0 else len(printQ) - 1
             
        

    print(result)
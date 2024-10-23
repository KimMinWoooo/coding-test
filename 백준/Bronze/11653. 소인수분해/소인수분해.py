n = int(input())
def solution(n):
    answer = []
    
    x = 2
    while x <= n:
        if n % x == 0:
            answer.append(x)
            print(x)
            n //= x
        else:
            x += 1
    return answer

solution(n)
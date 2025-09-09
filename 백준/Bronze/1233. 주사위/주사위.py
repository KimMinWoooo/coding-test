s1, s2, s3 = map(int, input().split()) # 3개의 주사위에 각각 s1개수의 면, s2 개수의 면 이 있는것 육면체가 아닌 느낌
arr = [0 for _ in range(s1+s2+s3 + 1)]
# 3개의 주사위를 동시에 던졌음
for A in range(1,s1+1):
    for B in range(1,s2+1):
        for C in range(1,s3+1):
            N = 0
            N = A+B+C
            arr[N] += 1
 
print(arr.index(max(arr)))



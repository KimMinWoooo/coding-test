n = int(input())
jik=[0]*(n+1)
jik[1] = 1
if n > 1:
    jik[2] = 2
for i in range(3, n+1):
    jik[i] = (jik[i-1]+jik[i-2]) % 10007

print(jik[n])


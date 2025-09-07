N = int(input())
cnt = 0
for tak in range(0, N+1):
    for young in range(0,N+1):
        for nam in range(0,N+1):
            if tak + young + nam == N:
                if nam >= young+2:
                    if tak != 0 and young != 0 and nam != 0:
                        if tak%2==0:
                            cnt += 1

print(cnt)

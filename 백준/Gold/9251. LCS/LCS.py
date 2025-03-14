a = list(str(input()))
b = list(str(input()))

dp = [[0 for _ in range(len(b)+1)]for _ in range(len(a)+1)]

for i in range(1,len(a) +1):
	for j in range(1,len(b) +1):
		if a[i-1] == b[j-1]: # 만약 1번 문장 i-1 번째 단어와 2번 문장 j-1 번째 단어와 같다면면
			dp[i][j] = dp[i-1][j-1]+ 1 # +1
		else: # 아니면 앞 전 값들 중 최고값을 부여여
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			
print(dp[len(a)][len(b)])
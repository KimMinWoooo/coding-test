# 알파벳 숫자 정의
alpha = '32123323322122122212111221'
a = input()
b = input()
s = []

# a, b의 영어를 위 alpha의 몇번째 자리에 있는지 체크해서 변경
for i in range(len(a)):
    s.append(int(alpha[ord(a[i])-65]))
    s.append(int(alpha[ord(b[i])-65]))
    
for i in range(len(a)+len(b)-1, 1, -1):
    ss = []
    for j in range(i):
        ss.append((s[j]+s[j+1])%10)
    s = ss
print(str(s[0])+str(s[1]))
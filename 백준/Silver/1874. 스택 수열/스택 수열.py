n = int(input())
stack = [] # 스택을 넣을 배열 변수
ans = [] # +, - 의 기호가 들어갈 변수
current = 1 # 스택에 들어갈 숫자 추적

for i in range(n):
    g = int(input())
    while current <= g:
        stack.append(current)
        ans.append("+")
        current += 1  # 예시 1번을 가정하면 ans에 4까지 +가 4개 들어감

    if stack[-1] == g: # 이때 -1 값이 4라면 pop하고 -를 ans에 넣어줌
        stack.pop()
        ans.append("-")
    else:
        print("NO") # 근데 g까지 current가 갔는데도 -1값이 g가 아니라면 NO
        break
else:
    for i in ans: # 배열로 들어간 +,- 기호들을 나열해줌
        print(i)

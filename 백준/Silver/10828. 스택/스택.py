# 입력을 정수로 받음 -> 받은 만큼 입력 (for문을 통한 반복?)
# 변수에 stack 입력들을 저장하자 
import sys
a = int(sys.stdin.readline())
k = [] # 스택

for _ in range(a):
    i = sys.stdin.readline().split()
# 명령을 처리하는 프로그램 -> 총 5개의 조건이 존재함 (if)
# 1. push : append() 
    if i[0] == 'push':
        k.append(int(i[1]))
# 2. pop : 맨 위 변수를 pop()으로
    elif i[0] == 'pop':
        if not k:
            print(-1)
        else:
            print(k[-1])
            k.pop()
# 3. size : 스택 크기 출력 -> len()
    elif i[0] == 'size':
        print(len(k))
# 4. empty : 조건넣어서 1 or 0
    elif i[0] == 'empty':
        if len(k) == 0:
            print(1)
        else:
            print(0)
# 5. top : pop이랑 비슷하지만 마지막에 출력만 하고 안뻄
    elif i[0] == 'top':
        if not k:
            print(-1)
        else:
            print(k[-1])




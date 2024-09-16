n = int(input())

theEndNumber = 666 # 번호
count = 0 # 번호를 업데이트 시켜줄 카운트값
while True:
    if '666' in str(theEndNumber):
        count += 1
        if count == n:
            break
    theEndNumber += 1

print(theEndNumber)
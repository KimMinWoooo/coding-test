def solution(answers): # 문제의 정답 answers [1,3,2,4,2]
    friend1 = [1,2,3,4,5]
    friend2 = [2,1,2,3,2,4,2,5]
    friend3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0]
    array =[]
    for i,answer in enumerate(answers):
        if answer == friend1[i%5]:
            scores[0] += 1
        if answer == friend2[i%8]:
            scores[1] += 1
        if answer == friend3[i%10]:
            scores[2] += 1
    for j in range(3):
        if scores[j] == max(scores):
            array.append(j+1)
    return array
    # 1번 친구와 answers 비교하기
    
        
    

# 문제의 입력 사항 : 문제의 정답
# 문제의 요구 사항 : 답을 가장 많이 맞춘 사람?
# 1번 친구 : 12345 반복
# 2번 친구 : 2 다음 1 2 다음 3.. 반복
# 3번 친구 : 3 1 2 4 5 두번씩 반복

# 최대 10000문제 , 답 가장 맞춘 사람 여러명이면 1번 친구부터 출력

# 문제의 정답을 알려줬을때 1번 친구, 2번 친구, 3번 친구 답 개수 확인하고 답 많이 맞춘 사람 출력
# 같으면 오름차순으로 출력
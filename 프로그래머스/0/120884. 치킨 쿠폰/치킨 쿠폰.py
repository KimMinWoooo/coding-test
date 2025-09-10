def solution(chicken):
    answer = 0
    while chicken >= 10:
        answer += chicken // 10 # 108 + 10 + 1 + 1
        chicken = chicken // 10 + chicken % 10 # 109 -> 19 -> 10
    return answer
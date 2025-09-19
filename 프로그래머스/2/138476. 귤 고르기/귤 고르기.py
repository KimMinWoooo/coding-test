from collections import Counter

def solution(k, tangerine):
    tangerine_counts = Counter(tangerine)
    sorted_counts = sorted(tangerine_counts.values(), reverse=True)
    answer = 0
    for count in sorted_counts:
        answer += 1
        k -= count
        if k <= 0:
            break
    return answer

# 귤을 k 개 만큼 담아서 팔고 싶다
# k 개를 담을때 분류 기준은 최대한 귤의 크기가 비슷하게 담고싶다
# 담았을때 종류의 개수가 맞지 않으면 버리기?
# 100,000개의 입력 -> 완전 탐색 x , 위 조건 처럼 되는 것부터 -> greedy
# 

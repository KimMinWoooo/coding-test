def solution(word):
    answer = 0
    char_map = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    weights = [781, 156, 31, 6, 1]
    
    for i in range(len(word)):
        char_order = char_map[word[i]]
        answer += weights[i] * char_order + 1
        
    return answer

# A -> E -> I -> O -> U 순서대로 5글자씩 단어 수록
# A로 시작하는 단어 부터 E로 시작하기 전까지 : 732
# 모든 단어를 만들어가면서 word에 해당되면 그 단어가 몇 번째인지 출력해주면 된다.
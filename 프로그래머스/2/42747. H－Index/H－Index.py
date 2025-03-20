# n편중 h 번이상 인용된 논문이 h 편이상
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
        
    return len(citations)
        
        
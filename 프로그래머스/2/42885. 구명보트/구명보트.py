def solution(people, limit):
    answer = 0
    new_people = sorted(people)
    s = 0
    e = len(new_people) - 1
    while s <= e:
        if new_people[s]+new_people[e] <= limit:
            answer += 1
            s += 1
            e -= 1
        else:
            answer += 1
            e -= 1
    
    
    return answer


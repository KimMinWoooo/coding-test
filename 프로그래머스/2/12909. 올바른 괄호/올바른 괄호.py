def solution(s):
    arr = []
    for i in s:
        if i == "(":
            arr.append(i)
        else:
            if arr == []:
                return False
            else:
                arr.pop()
    if arr == []:
        return True
    else:
        return False
        
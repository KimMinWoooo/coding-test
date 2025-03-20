def solution(numbers):
    strnum = [str(num) for num in numbers]
    strnum.sort(key=lambda num: num*3, reverse=True)
    return str(int("".join(strnum)))
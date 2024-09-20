def count_trailing_zeros(N):
    count = 0
    power_of_5 = 5
    while N >= power_of_5:
        count += N // power_of_5
        power_of_5 *= 5
    return count

N = int(input())  # N을 입력받음
print(count_trailing_zeros(N))  # N!의 뒤에 있는 연속된 0의 개수를 출력
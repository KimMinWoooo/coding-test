N = int(input())
first_arr=set(map(int, input().split()))
M = int(input())
second_arr=list(map(int, input().split()))

for i in second_arr:
    print(1) if i in first_arr else print(0)
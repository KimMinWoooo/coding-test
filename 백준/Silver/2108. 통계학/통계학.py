# 입력 : 수의 개수 N (무조건 홀수) 그다음 N줄만큼 정수들이 주어짐 (절대값 4000 안넘)
# 출력 
# 1번 줄: 산술평균 출력 소수점 이하 첫째자리에서 반올림한 값 - N개의 수들의 합을 N으로 나눈 값
#        다 더하고 N으로 나누기
# 2번 줄: 중앙값 출력 - N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
#        배열로 만들어서 중앙 값 나타내기
# 3번 줄: 최빈 값 출력 (여러개 있을때는 두번째로 작은 값 출력) - N개의 수들 중 가장 많이 나타내는 값
#        배열 탐색 실시하기?
# 4번 줄: 범위 출력 - N개의 수들 중 최댓값과 최솟값의 차이
#        max, min의 값 차이 나타내기

import sys
input = sys.stdin.readline
N = int(input())
col = []
for _ in range(N):
    A = int(input())
    col.append(A)

col.sort()
# [1, 3, 8, -2, 2]
# 1번 산술 평균 구하기
print(round(sum(col)/len(col))) 
# 2번 중앙 값 출력 하기
print(col[len(col)//2])
# 3번 최빈 값 출력 하기
dic = dict()
for i in col:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

mx = max(dic.values())
mx_dic = []

for i in dic:
    if mx == dic[i]:
        mx_dic.append(i)
if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])


# 4번 범위 출력
print(max(col)-min(col))


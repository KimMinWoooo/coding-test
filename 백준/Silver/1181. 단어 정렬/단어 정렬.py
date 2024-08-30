# 단어 개수 int
n = int(input())
# 단어 개수 n 만큼 단어를 써야함 -> for range n만큼
words = []

for i in range(n):
    words.append(input())

# 중복제거 및 길이 순서대로 sort -> set과 len길이 값을 이용한 sort
set_words = set(words)
words = list(set_words)
words.sort()
words.sort(key = len)

for i in words:
    print(i)
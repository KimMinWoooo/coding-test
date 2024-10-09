N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

sb= 0
for sz in size:
  if sz == 0:
    continue
  elif sz <= T:
    sb += 1
  elif sz % T == 0:
    sb += (sz // T)
  else:
    sb += (sz // T) + 1

print(sb)
print(N//P, N%P)
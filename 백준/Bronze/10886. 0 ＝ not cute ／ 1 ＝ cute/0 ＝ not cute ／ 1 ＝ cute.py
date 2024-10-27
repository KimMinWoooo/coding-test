N = int(input())
cute = 0
no = 0
for i in range(N):
    a = int(input())
    if a == 1:
        cute += 1
    else:
        no += 1

if cute > no:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")

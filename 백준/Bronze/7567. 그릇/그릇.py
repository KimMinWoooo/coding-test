dish = list(input())
result = 10
for i in range(1, len(dish)):
    if dish[i] == '(' and dish[i-1] == '(':
        result += 5
    elif dish[i] == ')' and dish[i-1] == '(':
        result += 10
    elif dish[i] == '(' and dish[i-1] == ')':
        result += 10
    else:
        result += 5
print(result)
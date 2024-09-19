while(1):
    pnt = input()
    if pnt == ".":
        break

    stack = []
    ans = True

    for sch in pnt:
        if sch == "(" or sch == "[":
            stack.append(sch)
        elif sch == "]":
            if len(stack) == 0 or stack[-1] == "(":
                ans = False
                break
            elif stack[-1] == "[":
                stack.pop()
        elif sch == ")":
            if len(stack) == 0 or stack[-1] == "[":
                ans = False
                break
            elif stack[-1] == "(":
                stack.pop()
    if len(stack) == 0 and ans == True:
        print('yes')
    else:
        print('no')
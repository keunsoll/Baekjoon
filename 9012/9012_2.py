
n = int(input())


for i in range(n):
    str = list(input())
    stack = []
    for i in str:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")

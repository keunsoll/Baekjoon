import sys

def push(x):
    stack.append(x)

def pop():
    if (len(stack)==0):
        return -1 
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    if (len(stack)==0):
        return 1
    else:
        return 0

def top():
    if (len(stack)==0):
        return -1
    else:
        return stack[-1]
n=int(sys.stdin.readline())
stack=[]
for i in range(n):
    command=sys.stdin.readline().split()
    ##print(command)


    if (command[0]=="push"):
        push(command[1])
    elif(command[0]=="pop"):
        print(pop())
    elif(command[0]=="size"):
        print(size())
    elif(command[0]=="empty"):
        print(empty())
    elif(command[0]=="top"):
        print(top())

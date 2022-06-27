import sys

que=[]
def push(x):
    que.append(x)

def pop():
    if que:
        print(que.pop(0))
    else:
        print(-1)

def size():
    print(len(que))

def empty():
    if que:
        print(0) 
    else:
        print(1)

def front():
    if que:
        print(que[0])
    else:
        print(-1)     

def back():
    if que:
        print(que[-1])
    else:
        print(-1)                          

input=sys.stdin.readline
n=int(input())
for i in range(n):
    command=input().split()

    if (command[0]=="push"):
        push(command[1])
    if (command[0]=="pop"):
        pop()
    if (command[0]=="size"):
        size()
    if (command[0]=="empty"):
        empty()
    if (command[0]=="front"):
        front()
    if (command[0]=="back"):
        back()

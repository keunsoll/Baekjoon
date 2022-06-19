import sys
from collections import deque
#dq=deque()

def push_front(x):
    dq.appendleft(x)

def push_back(x):
    dq.append(x)

def pop_front():
    if dq:
        print(dq.popleft())
    else:
        print(-1)    

def pop_back():
    if dq:
        print(dq.pop())
    else:
        print(-1)

def size():
    print(len(dq))

def empty():
    if dq:
        print(0)
    else:
        print(1)

def front():
    if dq:
        print(dq[0])
    else:
        print(-1)

def back():
    if dq:
        print(dq[-1])
    else:
        print(-1)   

n=int(sys.stdin.readline())
dq=deque()
for i in range(n):
    command=sys.stdin.readline().split()

    if (command[0]=="push_front"):
        push_front(command[1])
    if(command[0]=="push_back"):
        push_back(command[1])
    if(command[0]=="pop_front"):
        pop_front()
    if(command[0]=="pop_back"):
        pop_back()
    if(command[0]=="size"):
        size()
    if(command[0]=="empty"):
        empty()
    if(command[0]=="front"):
        front()
    if(command[0]=="back"):
        back()              
                
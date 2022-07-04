#참고
import sys
input=sys.stdin.readline

str=list(input().strip())
m=int(input())
sstr=[]

for i in range(m):
    command=input().strip()

    if command[0]=="L" and str!=[]:
        sstr.append(str.pop())
    elif command[0]=="D" and sstr!=[]:
        str.append(sstr.pop())    
    elif command[0]=="B" and str!=[]:
        str.pop()
    elif command[0]=="P":
        str.append(command[2])

print("".join(str+list(reversed(sstr))))
        
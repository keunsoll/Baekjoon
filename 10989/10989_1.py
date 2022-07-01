import sys
input=sys.stdin.readline

n=int(input())
numList=[0]*10001

for i in range(n):
    numList[int(input())]+=1 
    # 입력값을 받을 때마다 1을 더해줌 
    # ex) 7이 2번 입력되면 numList[7]에 2가 저장됨

for i in range(10001):
    if numList[i]!=0:
        for j in range(numList[i]):
            print(i)    


#<메모리 초과>
# n=int(input())
# numList=[]

## for 문 안에서 append를 사용하면 메모리 재할당으로 인해 메모리를 효율적으로 사용x
# for i in range(n):
#     numList.append(int(input()))

# ans=sorted(numList)
# for i in ans:
#     print(i)
    
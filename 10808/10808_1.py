s=input()
arr=[0 for i in range(26)]


for i in s:
    arr[ord(i)-ord('a')]+=1 ## ord(문자): 유니코드 정수를 반환/ord('a')==97
for i in arr:
    print(i, end=' ')
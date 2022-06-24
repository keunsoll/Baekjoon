s=list(input())

stack=[]
ans=0
for i in range(len(s)):
    if s[i]=='(': # 막대기 시작점
        stack.append(0)
    else: # ')' 일때
        if s[i-1]=='(': # 이전에 ( 이면 레이저
            stack.pop()
            ans+=len(stack)  
        else: # 이전에 ) 이면 막대기 끝부분
            stack.pop()
            ans+=1
print(ans)                  
        
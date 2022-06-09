s=input().upper() # 대문자로 변경
str=list(set(s)) # set(x) 함수: 리스트에서 중복요소 제거. 이때 x는 list 형태

c=[s.count(i) for i in str] # count(x): x가 리스트 안에 몇개 있는지 조사

'''
c=[]
for i in string:
    cnt=s.count(i)
    c.append(cnt)
'''
if c.count(max(c))>1:
    print("?")
else:
    print(str[c.index(max(c))]) # index(x): 리스트에서 x의 위치 반환       
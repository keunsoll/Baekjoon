n=int(input())
p_list=[]

def s(x):
    return x[0]
    

for i in range(n):
    age, name=map(str,input().split())
    age=int(age)
    p_list.append((age, name))

p_list.sort(key=s) ## key 값 기준으로 오름차순 정렬
 ## pl_list.sort(key= lamda x : x[0])

for i in p_list:
    print(i[0], i[1])

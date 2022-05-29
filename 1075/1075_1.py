# 십과 일의자리 00으로 초기화 후 하나씩 늘려가면서 나눠지는지 확인
# 나눠지는 수 십과 일의 자리 출력

N=int(input())
F=int(input())

N_list=list(map(int,str(N)))
N_list[-1]=0
N_list[-2]=0
n=0
for i in range(len(N_list)):
    n+=N_list[i]*(10**(len(N_list)-1-i))

#참고
while True:
    if n%F==0:
        break
    n+=1
print(str(n)[-2:])    



'''
for i in range(100):
    num=n+i
    if num%F==0:
        n_list=list(map(int,str(num)))
    else:
        continue   

        
print(n_list)
'''


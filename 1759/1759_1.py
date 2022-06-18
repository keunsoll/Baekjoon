import itertools
l,c=map(int,input().split())
str=sorted(input().split())
code=itertools.combinations(str,l)

for alpha in code:
    vow=0
    for i in alpha:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vow+=1
    if vow>=1 and l-vow>=2: #최소 한개 이상의 모음, 2개 이상의 자음
        print(''.join(alpha))        


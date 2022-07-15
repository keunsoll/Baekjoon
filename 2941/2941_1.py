word=input()

c_alpha=["c=", "c-", "dz=","d-", "lj", "nj", "s=", "z=" ]
for i in c_alpha:
    word=word.replace(i,'a') #바꿀 문자는 어떤 문자이든 상관없음
    # replace(old, new, [count])
    ## old: 현재 문자열에서 변경하고 싶은 문자
    ## new: 새로 바꿀 문자
    ## count: 변경할 횟수. 입력하지 않으면 전체 변경
print(len(word))
 
s=input().split() 
# 문자열.split(sep, maxsplit)
## maxsplit은 횟수만큼, sep의 구분자를 기준으로 문자열을 구분하여 잘라서 리스트로 만들어줌
### sep : 기본 값 none(띄어쓰기, 엔터를 구분자로)
### 문자열.split(sep=',') / sep 생략 가능: 문자열.split(',')
#### maxsplit : 기본값 -1(자를 수 있을 때까지 문자열 전체를 자름)
#### 문자열.split(maxsplit=1) : 문자열을 한번만 자름 / maxsplit 생략시 앞에 sep이 있어야함. 문자열.split(',', 1)

print(len(s))
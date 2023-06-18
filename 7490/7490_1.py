# 참고
import copy

# 아스키 코드 순으로 백트래킹하며 수식 생성


def back_tracking(v):

    # 수식 개수가 n -1 개면 수식을 arr에 추가
    if len(v) == n - 1:
        arr.append(copy.deepcopy(v))
        # print("arr:", arr)
        return
    # 아스키 코드 34
    v.append(' ')
    back_tracking(v)
    # print(v)
    v.pop()

    # 아스키 코드 44
    v.append('+')
    back_tracking(v)
    # print(v)
    v.pop()

    # 아스키 코드 45
    v.append('-')
    back_tracking(v)
    # print(v)
    v.pop()


test = int(input())

for _ in range(test):
    n = int(input())
    arr = []
    back_tracking([])
    print(arr)
    # 모든 수식을 확인
    for i in arr:
        temp = ""
        # 수식을 숫자 사이 사이에 추가
        for j in range(1, n):
            temp += str(j) + str(i[j - 1])
        temp += str(n)
        print(temp)

        # eval를 통해 수식을 더한 수가 0 인지 비교
        # replace는 공백을 제거하기 위해
        if eval(temp.replace(' ', '')) == 0:
            print(temp)

    print()

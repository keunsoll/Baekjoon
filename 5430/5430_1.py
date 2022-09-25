t = int(input())

# def R(a):

for i in range(t):
    func = list(input())
    size = int(input())
    arr = list(map(int, input()[1:-1].replace(",", "")))

    for j in range(len(func)):
        if func[j] == "R":
            if len(arr) == 0:
                print(arr)
                break
            arr = arr[::-1]
        elif func[j] == "D":
            if len(arr) == 0:
                print("error")
                break
            arr.pop(0)
    else:
        if len(arr) == 0:
            print('error')
        else:
            print(arr)


# 1. r d 함수 설계 r: reverse d: pop.left(비어 있으면 error)-> 배열 자체가 0이면 빈배열
#

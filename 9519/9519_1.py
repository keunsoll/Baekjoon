n = int(input())
word = list(input())


def find(word):
    front = []
    back = []

    for i in range(len(word)):
        if i % 2 == 0:
            front.append(word[i])
            # print(front)
        else:
            back.append(word[i])
            # print(back)
    back = back[::-1]
    return "".join(front)+"".join(back)


ans = []
ans.append("".join(word))


for i in range(n):
    word = find(word)
    print(word)

    # 같은 단어가 나오면 중지 -> 주기 한 바퀴 돎
    if word in ans:
        break

    ans.append(word)
print(ans)

per = len(ans)
print(ans[n % per])

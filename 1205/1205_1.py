n, taesu, p = map(int, input().split())


# print(score)


if n == 0:
    print(1)
else:
    rank = 0
    score = list(map(int, input().split()))
    if n == p and score[-1] >= taesu:
        rank = -1
    else:
        for i in range(len(score)):
            if score[i] <= taesu:
                rank = i+1
                break
            # 새로운 점수보다 작거나 같은 점수가 없을 때 가장 낮은 등수
            else:
                rank = n+1

    print(rank)

n, taesu, p = map(int, input().split())
score = list(map(int, input().split()))
# print(score)

rank = 0
if not score:
    print(1)
else:
    if n == p and score[-1] >= taesu:
        rank = -1
    else:
        for i in range(len(score)):
            if score[i] <= taesu:
                rank = i+1
                break

    print(rank)

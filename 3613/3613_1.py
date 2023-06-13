s = input()

# C 입력
if '_' in s and s.islower():
    # _가 맨 앞에 있거나 맨 뒤에 있을 때
    if s.index('_') == 0 or s.index('_') == (len(s)-1):
        print("Error!")
    else:
        # _가 연속으로 두 개이상 있을 때
        cnt = 0
        for i in range(1, len(s)):
            if s[i] == '_':
                cnt += 1
            else:
                cnt = 0
            if cnt > 1:
                print("Error!")
                break
        else:
            c = s.split('_')

            for i in range(1, len(c)):
                c[i] = c[i].capitalize()
            print("".join(c))

# JAVA 입력
else:
    j = []
    if not '_' in s and s[0].islower():
        prev = 0
        for i in range(len(s)):
            if s[i].isupper():
                j.append(s[prev:i])
                prev = i
        j.append(s[prev:])  # 마지막 단어

        for i in range(1, len(j)):
            j[i] = j[i].lower()
        print('_'.join(j))
    else:
        print("Error!")

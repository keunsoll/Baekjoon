s = input()

if '_' in s and s.islower():
    if s.index('_') == 0 or s.index('_') == (len(s)-1):
        print("Error!")
    else:
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

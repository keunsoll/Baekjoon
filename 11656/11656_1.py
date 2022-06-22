s=input()

suf=[]
for i in range(len(s)):
    suf.append(s[i:])
suf.sort()

for i in suf:
    print(i)   



s=input()
arr=[-1 for i in range(26)]

for i in range(len(s)):
    if arr[ord(s[i])-ord('a')] == -1:
        arr[ord(s[i])-ord('a')]=i

for i in arr:
    print(i, end=' ')

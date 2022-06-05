n=int(input())
for i in range(n):
    count, ch=input().split()
    for j in ch:
        print(j*int(count), end="")
    print()    

    
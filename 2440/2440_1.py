a=int(input())

for i in range(1, a+1):
    for j in range(a+1-i):
        print("*", end="")
    print("")  
while True:
    try:
        l=0
        u=0 
        d=0
        s=0
        str=input()
        for i in range(len(str)):
            if str[i].islower():
                l+=1
            elif str[i].isupper():
                u+=1
            elif str[i].isdigit():
                d+=1
            elif str[i].isspace():
                s+=1
        print(l,u,d,s)
    except EOFError:
        break                        

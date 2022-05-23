s=input()

string=''
for i in range(len(s)):
    if s[i]== ' ' or ord(s[i]) < ord('A'):
        string+=s[i]
    else:
        if ord(s[i])+13>122:
            string+=chr(96+(ord(s[i])+13)-122)
        elif ord(s[i])+13>90 and ord(s[i])<91:
            string+=chr(64+(ord(s[i])+13)-90)
        else:
            string+=chr(ord(s[i])+13)           
print(string)             



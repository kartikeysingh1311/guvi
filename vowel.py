x=str(input())
if ((x>='a' and x<='z') or (x>='A' and x<='Z')) and len(x)==1:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
        print("vowel")
    else:
        print("consonant")
else:
    print("invalid")

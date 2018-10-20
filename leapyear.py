x=int(input())
if x%100==0 and x%400!=0:
    print("not leap")
elif x%4==0:
    print("leap")
else:
    print("not leap")

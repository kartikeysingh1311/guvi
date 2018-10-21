n=int(input())
k=int(input())
if k>n:
    print("error")
else:
    l=[]
    sum=0
    for i in range(n):
        x=int(input())
        l.append(x)
    for i in range(k):
        sum+=l[i]
    print(sum)

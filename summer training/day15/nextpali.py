n=int(input())
m=n
while(1):
    rev=0
    temp=n
    while(temp>0):
        x=temp%10
        rev=rev*10+x
        temp=temp//10
    
    if(rev==n):
        print(rev)
        break
    else:
        n=n+1
   